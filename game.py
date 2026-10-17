<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>🔥 عباس خان فائر ایڈونچر</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: linear-gradient(135deg, #1a0a00 0%, #3d1a00 50%, #1a0a00 100%);
            overflow: hidden;
            font-family: 'Arial', sans-serif;
            touch-action: none;
        }

        #gameCanvas {
            display: block;
            margin: 0 auto;
            background: radial-gradient(ellipse at center, #3d1a00 0%, #1a0a00 100%);
        }

        #welcomeScreen {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, rgba(255, 100, 0, 0.9), rgba(255, 50, 0, 0.9));
            padding: 40px;
            border-radius: 30px;
            border: 4px solid #ffaa00;
            box-shadow: 0 0 50px rgba(255, 100, 0, 0.8), 0 0 100px rgba(255, 50, 0, 0.5);
            text-align: center;
            color: white;
            z-index: 100;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: translate(-50%, -50%) scale(1); }
            50% { transform: translate(-50%, -50%) scale(1.05); }
        }

        #welcomeScreen h1 {
            font-size: 48px;
            color: #ffdd00;
            text-shadow: 0 0 20px #ffdd00, 0 0 40px #ffaa00, 0 0 60px #ff6600;
            margin-bottom: 20px;
            animation: glow 1.5s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 20px #ffdd00, 0 0 40px #ffaa00; }
            to { text-shadow: 0 0 30px #ffdd00, 0 0 60px #ffaa00, 0 0 80px #ff6600; }
        }

        #welcomeScreen p {
            font-size: 24px;
            color: #ffffff;
            text-shadow: 0 0 10px #ffffff, 0 0 20px #ffaa00;
            margin: 15px 0;
        }

        #playerName {
            font-size: 56px;
            font-weight: bold;
            color: #ffdd00;
            text-shadow: 0 0 30px #ffdd00, 0 0 60px #ffaa00, 0 0 90px #ff6600;
            margin: 30px 0;
            padding: 20px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 20px;
            border: 3px solid #ffdd00;
        }

        button {
            background: linear-gradient(45deg, #ff6600, #ffaa00, #ffdd00);
            border: none;
            padding: 20px 60px;
            color: #1a0a00;
            font-size: 28px;
            font-weight: bold;
            border-radius: 50px;
            cursor: pointer;
            margin-top: 30px;
            box-shadow: 0 0 30px rgba(255, 100, 0, 0.8), 0 0 60px rgba(255, 170, 0, 0.5);
            transition: all 0.3s;
            animation: buttonGlow 2s infinite;
        }

        @keyframes buttonGlow {
            0%, 100% { box-shadow: 0 0 30px rgba(255, 100, 0, 0.8), 0 0 60px rgba(255, 170, 0, 0.5); }
            50% { box-shadow: 0 0 50px rgba(255, 100, 0, 1), 0 0 100px rgba(255, 170, 0, 0.8); }
        }

        button:hover {
            transform: scale(1.1);
            box-shadow: 0 0 60px rgba(255, 100, 0, 1), 0 0 120px rgba(255, 170, 0, 1);
        }

        #ui {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            color: #ffdd00;
            font-size: 28px;
            text-shadow: 0 0 10px #ffdd00, 0 0 20px #ffaa00;
            z-index: 10;
            text-align: center;
            background: rgba(0, 0, 0, 0.5);
            padding: 15px 30px;
            border-radius: 20px;
            border: 2px solid #ffaa00;
        }

        #gameOverScreen {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, rgba(255, 50, 0, 0.95), rgba(100, 0, 0, 0.95));
            padding: 40px;
            border-radius: 30px;
            border: 4px solid #ff0000;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.8);
            text-align: center;
            color: white;
            z-index: 100;
            display: none;
        }

        #gameOverScreen h2 {
            font-size: 42px;
            color: #ffdd00;
            text-shadow: 0 0 20px #ffdd00, 0 0 40px #ff0000;
            margin-bottom: 20px;
        }

        .hidden {
            display: none !important;
        }
    </style>
</head>
<body>
    <div id="welcomeScreen">
        <h1>🔥 خوش آمدید 🔥</h1>
        <p>فائر ایڈونچر گیم میں</p>
        <div id="playerName">عباس خان</div>
        <p>🎮 تیار ہو جائیں!</p>
        <button onclick="startGame()">🚀 گیم شروع کریں</button>
    </div>

    <div id="ui" class="hidden">
        <div>🔥 اسکور: <span id="score">0</span></div>
        <div>⚡ لیول: <span id="level">1</span></div>
        <div>❤️ زندگی: <span id="lives">3</span></div>
    </div>

    <div id="gameOverScreen">
        <h2>😢 گیم ختم!</h2>
        <p style="font-size: 32px; margin: 20px 0;">عباس خان</p>
        <p style="font-size: 28px;">آپ کا اسکور: <span id="finalScore" style="color: #ffdd00; font-weight: bold;">0</span></p>
        <p style="font-size: 24px;">لیول: <span id="finalLevel">1</span></p>
        <button onclick="restartGame()">🔄 دوبارہ کھیلیں</button>
    </div>

    <canvas id="gameCanvas"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreEl = document.getElementById('score');
        const levelEl = document.getElementById('level');
        const livesEl = document.getElementById('lives');
        const welcomeScreen = document.getElementById('welcomeScreen');
        const gameOverScreen = document.getElementById('gameOverScreen');
        const finalScoreEl = document.getElementById('finalScore');
        const finalLevelEl = document.getElementById('finalLevel');
        const ui = document.getElementById('ui');

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);

        let player = { x: 0, y: 0, size: 50, color: '#ff6600', speed: 8 };
        let fireballs = [];
        let enemies = [];
        let particles = [];
        let score = 0;
        let level = 1;
        let lives = 3;
        let gameRunning = false;
        let animationId;
        let enemySpeed = 4;
        let spawnRate = 50;
        let frameCount = 0;
        let canShoot = true;
        let shootCooldown = 15;
        let shootTimer = 0;

        function createExplosion(x, y, color, count = 20) {
            for (let i = 0; i < count; i++) {
                particles.push({
                    x: x,
                    y: y,
                    vx: (Math.random() - 0.5) * 15,
                    vy: (Math.random() - 0.5) * 15,
                    life: 1,
                    color: color,
                    size: Math.random() * 8 + 4
                });
            }
        }

        function updatePlayer(inputX, inputY) {
            const dx = inputX - player.x;
            const dy = inputY - player.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance > 5) {
                player.x += (dx / distance) * player.speed;
                player.y += (dy / distance) * player.speed;
            }

            if (player.x < player.size) player.x = player.size;
            if (player.x > canvas.width - player.size) player.x = canvas.width - player.size;
            if (player.y < player.size) player.y = player.size;
            if (player.y > canvas.height - player.size) player.y = canvas.height - player.size;
        }

        function shootFireball() {
            if (shootTimer <= 0) {
                fireballs.push({
                    x: player.x,
                    y: player.y - player.size,
                    vx: 0,
                    vy: -15,
                    size: 20,
                    color: '#ffdd00'
                });
                shootTimer = shootCooldown;
                createExplosion(player.x, player.y - player.size, '#ffaa00', 10);
            }
        }

        function spawnEnemy() {
            const size = Math.random() * 50 + 30;
            enemies.push({
                x: Math.random() * (canvas.width - size),
                y: -size,
                size: size,
                speed: enemySpeed + Math.random() * 3,
                color: `hsl(${Math.random() * 30}, 100%, 50%)`,
                health: Math.floor(level / 2) + 1
            });
        }

        function checkCollision(circle1, circle2) {
            const dx = circle1.x - circle2.x;
            const dy = circle1.y - circle2.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            return distance < (circle1.size + circle2.size);
        }

        function drawFireEffect(x, y, size, color) {
            const gradient = ctx.createRadialGradient(x, y, 0, x, y, size);
            gradient.addColorStop(0, '#ffdd00');
            gradient.addColorStop(0.3, '#ffaa00');
            gradient.addColorStop(0.6, '#ff6600');
            gradient.addColorStop(1, 'transparent');
            
            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(x, y, size, 0, Math.PI * 2);
            ctx.fill();
        }

        function gameLoop() {
            if (!gameRunning) return;

            ctx.fillStyle = 'rgba(26, 10, 0, 0.2)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            frameCount++;
            shootTimer = Math.max(0, shootTimer - 1);

            if (frameCount % spawnRate === 0) {
                spawnEnemy();
            }

            particles.forEach((particle, index) => {
                particle.x += particle.vx;
                particle.y += particle.vy;
                particle.vy += 0.3;
                particle.life -= 0.03;
                particle.size *= 0.95;

                if (particle.life <= 0) {
                    particles.splice(index, 1);
                    return;
                }

                drawFireEffect(particle.x, particle.y, particle.size, particle.color);
            });

            fireballs.forEach((fireball, fbIndex) => {
                fireball.x += fireball.vx;
                fireball.y += fireball.vy;

                drawFireEffect(fireball.x, fireball.y, fireball.size, fireball.color);

                enemies.forEach((enemy, eIndex) => {
                    if (checkCollision(fireball, enemy)) {
                        fireballs.splice(fbIndex, 1);
                        enemy.health--;
                        createExplosion(fireball.x, fireball.y, '#ffdd00', 15);

                        if (enemy.health <= 0) {
                            enemies.splice(eIndex, 1);
                            createExplosion(enemy.x, enemy.y, enemy.color, 30);
                            score += 20;
                            scoreEl.textContent = score;

                            if (score % 200 === 0) {
                                level++;
                                levelEl.textContent = level;
                                enemySpeed += 0.5;
                                spawnRate = Math.max(20, spawnRate - 5);
                                lives = Math.min(5, lives + 1);
                                livesEl.textContent = lives;
                                createExplosion(player.x, player.y, '#00ff00', 50);
                            }
                        }
                        return;
                    }
                });

                if (fireball.y < 0 || fireball.x < 0 || fireball.x > canvas.width) {
                    fireballs.splice(fbIndex, 1);
                }
            });

            enemies.forEach((enemy, index) => {
                enemy.y += enemy.speed;

                drawFireEffect(enemy.x, enemy.y, enemy.size, enemy.color);

                if (checkCollision(player, enemy)) {
                    enemies.splice(index, 1);
                    lives--;
                    livesEl.textContent = lives;
                    createExplosion(player.x, player.y, '#ff0000', 40);

                    if (lives <= 0) {
                        gameOver();
                        return;
                    }
                }

                if (enemy.y > canvas.height + enemy.size) {
                    enemies.splice(index, 1);
                    lives--;
                    livesEl.textContent = lives;

                    if (lives <= 0) {
                        gameOver();
                        return;
                    }
                }
            });

            drawFireEffect(player.x, player.y, player.size + 20, '#ff6600');
            drawFireEffect(player.x, player.y, player.size, '#ffaa00');
            drawFireEffect(player.x, player.y, player.size - 10, '#ffdd00');

            ctx.fillStyle = '#ffffff';
            ctx.beginPath();
            ctx.arc(player.x, player.y, player.size - 20, 0, Math.PI * 2);
            ctx.fill();

            animationId = requestAnimationFrame(gameLoop);
        }

        let inputX = canvas.width / 2;
        let inputY = canvas.height - 100;
        let isTouching = false;

        canvas.addEventListener('touchstart', (e) => {
            e.preventDefault();
            isTouching = true;
            const touch = e.touches[0];
            inputX = touch.clientX;
            inputY = touch.clientY;
            shootFireball();
        });

        canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            if (isTouching) {
                const touch = e.touches[0];
                inputX = touch.clientX;
                inputY = touch.clientY;
                updatePlayer(inputX, inputY);
            }
        });

        canvas.addEventListener('touchend', () => {
            isTouching = false;
        });

        canvas.addEventListener('mousedown', (e) => {
            inputX = e.clientX;
            inputY = e.clientY;
            shootFireball();
        });

        canvas.addEventListener('mousemove', (e) => {
            inputX = e.clientX;
            inputY = e.clientY;
            updatePlayer(inputX, inputY);
        });

        canvas.addEventListener('keydown', (e) => {
            if (e.code === 'Space') {
                shootFireball();
            }
        });

        function startGame() {
            welcomeScreen.classList.add('hidden');
            ui.classList.remove('hidden');
            gameRunning = true;
            score = 0;
            level = 1;
            lives = 3;
            enemySpeed = 4;
            spawnRate = 50;
            fireballs = [];
            enemies = [];
            particles = [];
            scoreEl.textContent = score;
            levelEl.textContent = level;
            livesEl.textContent = lives;
            inputX = canvas.width / 2;
            inputY = canvas.height - 100;
            player.x = inputX;
            player.y = inputY;
            gameLoop();
        }

        function gameOver() {
            gameRunning = false;
            cancelAnimationFrame(animationId);
            ui.classList.add('hidden');
            finalScoreEl.textContent = score;
            finalLevelEl.textContent = level;
            gameOverScreen.style.display = 'block';
        }

        function restartGame() {
            gameOverScreen.style.display = 'none';
            startGame();
        }
    </script>
</body>
</html>