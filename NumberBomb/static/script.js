// 游戏开始，请求后端初始化
fetch("http://127.0.0.1:5000/start")
    .then(res => res.json())
    .then(data => console.log(data.message));

// 获取页面元素
let input = document.getElementById("user_input");
let feedback = document.getElementById("feedback");
let countDisplay = document.getElementById("count");
let rangeDisplay = document.getElementById("range");
let binaryDisplay = document.getElementById("binary_search");
let submitBtn = document.getElementById("submit");

// 记录当前范围
let currentLeft = 1;
let currentRight = 100;

// 点击提交按钮
submitBtn.addEventListener("click", function () {
    let number = parseInt(input.value);

    // 输入校验
    if (isNaN(number)) {
        feedback.textContent = "请输入有效数字！";
        return;
    }
    if (number < currentLeft || number > currentRight) {
        feedback.textContent = `请输入范围 [${currentLeft}, ${currentRight}] 内的数字！`;
        return;
    }

    // 发送给Python后端
    fetch("http://127.0.0.1:5000/guess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ number: number })
    })
    .then(res => res.json())
    .then(data => {
        countDisplay.textContent = `已猜测次数：${data.count}`;

        if (data.result === "small") {
            currentLeft = data.left;
            feedback.textContent = "数字小了！";
            rangeDisplay.textContent = `范围：[${currentLeft}, ${currentRight}]`;
        } else if (data.result === "big") {
            currentRight = data.right;
            feedback.textContent = "数字大了！";
            rangeDisplay.textContent = `范围：[${currentLeft}, ${currentRight}]`;
        } else if (data.result === "correct") {
            feedback.textContent = `🎉 猜对了！你一共猜了 ${data.count} 次！`;
            submitBtn.disabled = true;
            binaryDisplay.textContent = `二分搜索顺序：${data.binary_list.join(" → ")}（共 ${data.binary_list.length} 次）`;
        }
    });

    input.value = "";
});

document.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        submitBtn.click();
    }
});