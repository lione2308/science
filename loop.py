import streamlit as st
import streamlit.components.v1 as components

# --- 1. 페이지 설정 ---
st.set_page_config(
    page_title="스트림릿 벽돌깨기",
    page_icon="🧱",
    layout="centered"  # 중앙 정렬
)

# --- 2. 게임 로직 (HTML/CSS/JavaScript) ---
# 이 모든 코드는 하나의 HTML 문자열로 처리됩니다.
game_html = """
<!DOCTYPE html>
<html>
<head>
    <title>벽돌깨기</title>
    <meta charset="utf-8">
    <style>
        /* CSS: 게임 캔버스를 가운데 정렬하고 배경색 지정 */
        body {
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 20px;
            overflow: hidden; /* 스크롤바 숨김 */
        }
        canvas {
            background: #111; /* 캔버스 배경은 검은색 */
            display: block;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<canvas id="gameCanvas" width="600" height="450"></canvas>

<script>
    // --- JavaScript 게임 로직 시작 ---

    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    // --- 게임 변수 (상태) ---
    let ballRadius = 10;
    let x = canvas.width / 2;
    let y = canvas.height - 30;
    let dx = 3; // 공의 x축 속도
    let dy = -3; // 공의 y축 속도

    // 패들(막대)
    let paddleHeight = 12;
    let paddleWidth = 100;
    let paddleX = (canvas.width - paddleWidth) / 2;

    // 벽돌
    let brickRowCount = 4;
    let brickColumnCount = 7;
    let brickWidth = 70;
    let brickHeight = 18;
    let brickPadding = 10;
    let brickOffsetTop = 30;
    let brickOffsetLeft = 30;

    let score = 0;
    let lives = 3;

    // 벽돌 배열 초기화 (2차원 배열)
    let bricks = [];
    for (let c = 0; c < brickColumnCount; c++) {
        bricks[c] = [];
        for (let r = 0; r < brickRowCount; r++) {
            // status: 1 = 살아있음, 0 = 깨짐
            bricks[c][r] = { x: 0, y: 0, status: 1 };
        }
    }

    // --- 이벤트 리스너 (마우스) ---
    // 마우스 움직임에 따라 패들 위치 변경
    document.addEventListener("mousemove", mouseMoveHandler, false);

    function mouseMoveHandler(e) {
        // 캔버스 좌측 경계 기준 마우스 위치 계산
        // (Streamlit iframe 내에서도 잘 동작하도록 getBoundingClientRect 사용)
        let relativeX = e.clientX - canvas.getBoundingClientRect().left;
        if (relativeX > 0 && relativeX < canvas.width) {
            paddleX = relativeX - paddleWidth / 2;
            // 패들이 캔버스 밖으로 나가지 않게
            if (paddleX < 0) paddleX = 0;
            if (paddleX + paddleWidth > canvas.width) paddleX = canvas.width - paddleWidth;
        }
    }

    // --- 그리기 함수들 ---

    function drawBall() {
        ctx.beginPath();
        ctx.arc(x, y, ballRadius, 0, Math.PI * 2);
        ctx.fillStyle = "#0095DD"; // 파란색 공
        ctx.fill();
        ctx.closePath();
    }

    function drawPaddle() {
        ctx.beginPath();
        ctx.rect(paddleX, canvas.height - paddleHeight, paddleWidth, paddleHeight);
        ctx.fillStyle = "#0095DD"; // 파란색 패들
        ctx.fill();
        ctx.closePath();
    }

    function drawBricks() {
        for (let c = 0; c < brickColumnCount; c++) {
            for (let r = 0; r < brickRowCount; r++) {
                if (bricks[c][r].status == 1) { // 살아있는 벽돌만 그리기
                    let brickX = (c * (brickWidth + brickPadding)) + brickOffsetLeft;
                    let brickY = (r * (brickHeight + brickPadding)) + brickOffsetTop;
                    bricks[c][r].x = brickX;
                    bricks[c][r].y = brickY;
                    ctx.beginPath();
                    ctx.rect(brickX, brickY, brickWidth, brickHeight);
                    ctx.fillStyle = "#DD4400"; // 주황색 벽돌
                    ctx.fill();
                    ctx.closePath();
                }
            }
        }
    }

    function drawScore() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#FFF"; // 흰색 글씨
        ctx.fillText("Score: " + score, 8, 20);
    }

    function drawLives() {
        ctx.font = "16px Arial";
        ctx.fillStyle = "#FFF";
        ctx.fillText("Lives: " + lives, canvas.width - 65, 20);
    }

    // --- 충돌 감지 로직 ---

    function collisionDetection() {
        for (let c = 0; c < brickColumnCount; c++) {
            for (let r = 0; r < brickRowCount; r++) {
                let b = bricks[c][r];
                if (b.status == 1) {
                    // 공이 벽돌의 범위 안에 있는지 확인
                    if (x > b.x && x < b.x + brickWidth && y > b.y && y < b.y + brickHeight) {
                        dy = -dy; // y축 방향 반전
                        b.status = 0; // 벽돌 깨짐
                        score++;
                        // 모든 벽돌을 깼는지 확인
                        if (score == brickRowCount * brickColumnCount) {
                            alert("YOU WIN, CONGRATULATIONS!");
                            document.location.reload();
                        }
                    }
                }
            }
        }
    }

    // --- 메인 게임 루프 ---

    function draw() {
        // 1. 화면 지우기
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // 2. 그리기
        drawBricks();
        drawBall();
        drawPaddle();
        drawScore();
        drawLives();
        
        // 3. 충돌 감지
        collisionDetection();

        // 4. 공 위치 업데이트
        
        // 좌우 벽 충돌
        if (x + dx > canvas.width - ballRadius || x + dx < ballRadius) {
            dx = -dx;
        }

        // 위쪽 벽 충돌
        if (y + dy < ballRadius) {
            dy = -dy;
        } 
        // 아래쪽 경계
        else if (y + dy > canvas.height - ballRadius) {
            // 패들에 맞았는지 확인
            if (x > paddleX && x < paddleX + paddleWidth) {
                dy = -dy; // 방향 반전
            } 
            // 못 맞음 (게임 오버)
            else {
                lives--;
                if (lives <= 0) {
                    alert("GAME OVER");
                    document.location.reload(); // 게임 재시작
                } else {
                    // 공, 패들 위치 초기화
                    x = canvas.width / 2;
                    y = canvas.height - 30;
                    dx = 3;
                    dy = -3;
                    paddleX = (canvas.width - paddleWidth) / 2;
                }
            }
        }

        x += dx;
        y += dy;

        // 5. 다음 프레임 요청 (이것이 게임 루프의 핵심)
        requestAnimationFrame(draw);
    }

    // 게임 시작
    draw();
