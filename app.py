import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 설정 (넓은 화면 모드 및 타이틀 아이콘 지정)
st.set_page_config(
    page_title="분수대에 동전 던지기 - 물리학 2 시뮬레이터",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 웹 브라우저 탭 및 메인 영역 스타일링을 위한 얇은 여백 추가
st.markdown("""
    <style>
        /* Streamlit 기본 패딩 최소화 및 배경 매칭 */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        iframe {
            border-radius: 12px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_value=True)

# 3. 임베딩할 고해상도 HTML5/CSS3/JavaScript 물리학 엔진 소스코드
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fountain Coin Toss - 물리 실시간 시뮬레이터</title>
    <!-- Tailwind CSS 및 아이콘 폰트 로드 -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');
        body {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: #0b0f19;
            color: #f1f5f9;
            overflow: hidden;
        }
        /* 프리미엄 글래스모피즘 효과 */
        .glass {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .glass-bright {
            background: rgba(30, 41, 59, 0.85);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        /* 대리석 물결 및 분수 애니메이션 키프레임 */
        @keyframes ripple {
            0% { transform: scale(0.9); opacity: 0.6; }
            50% { transform: scale(1.1); opacity: 0.9; }
            100% { transform: scale(0.9); opacity: 0.6; }
        }
        .water-ripple {
            animation: ripple 3s infinite ease-in-out;
        }
        /* 커스텀 슬라이더 트랙 커스터마이징 */
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #f59e0b;
            cursor: pointer;
            box-shadow: 0 0 8px rgba(245, 158, 11, 0.5);
            transition: transform 0.1s;
        }
        input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.2);
        }
    </style>
</head>
<body class="h-screen w-full flex flex-col justify-between p-4">

    <!-- 최상단 헤더 정보 표시 바 -->
    <header class="glass rounded-2xl px-6 py-3 flex justify-between items-center border border-slate-800/80 mb-2">
        <div class="flex items-center gap-3">
            <div class="bg-gradient-to-tr from-amber-500 to-yellow-600 p-2 rounded-xl shadow-md">
                <i class="fa-solid fa-coins text-white text-md"></i>
            </div>
            <div>
                <span class="text-[9px] text-amber-400 font-bold uppercase tracking-wider block">Physics Simulator</span>
                <h1 class="text-sm md:text-base font-black tracking-tight text-white">Fountain Coin Toss v2.0</h1>
            </div>
        </div>
        <div class="flex gap-4 text-xs">
            <div class="flex items-center gap-2">
                <span class="text-slate-400 font-bold">진행 레벨:</span>
                <span id="game-level" class="text-cyan-400 font-black">Level 1</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-slate-400 font-bold">최고 점수:</span>
                <span id="best-score" class="text-yellow-400 font-black">0</span>
            </div>
        </div>
    </header>

    <!-- 중앙 메인 작업 영역 -->
    <main class="flex-grow grid grid-cols-1 lg:grid-cols-4 gap-4 h-[calc(100%-120px)] overflow-hidden">
        
        <!-- 왼쪽/가운데: 캔버스 및 발사 조정 슬라이더 (3개 열 차지) -->
        <div class="lg:col-span-3 flex flex-col gap-4 h-full">
            
            <!-- 물리 시뮬레이션 메인 캔버스 뷰포트 -->
            <div class="relative glass rounded-3xl border border-slate-800/60 overflow-hidden flex-grow flex flex-col justify-between">
                <!-- 그라데이션 물리 공간 배경 -->
                <div class="absolute inset-0 bg-gradient-to-b from-slate-950 via-slate-900 to-cyan-950/10 -z-10"></div>
                
                <!-- 실시간 바람 벡터 디스플레이 -->
                <div id="wind-badge" class="absolute top-4 right-4 bg-slate-950/80 border border-slate-800 text-slate-300 rounded-xl px-3 py-1.5 text-xs flex items-center gap-2 z-10 hidden animate-pulse">
                    <i class="fa-solid fa-wind text-sky-400"></i>
                    <span>풍향 저항: <b id="wind-text" class="text-sky-400">0.0 m/s²</b></span>
                </div>

                <!-- 환경 상태 계측값 실시간 오버레이 -->
                <div class="absolute top-4 left-4 text-[10px] text-slate-500 font-mono space-y-0.5 z-10 pointer-events-none">
                    <div>중력 가속도(g) = <span id="env-g">9.80</span> m/s²</div>
                    <div>공기 저항 상수(k) = <span id="env-k">0.00</span></div>
                </div>

                <!-- 메인 그래픽 렌더링 캔버스 -->
                <canvas id="physics-canvas" class="w-full h-full cursor-crosshair"></canvas>
                
                <!-- 실시간 포물선 궤적 수치 예측 정보창 -->
                <div class="absolute bottom-4 right-4 glass-bright rounded-2xl p-3 text-[11px] space-y-1 text-slate-300 pointer-events-none w-44 border border-white/5 shadow-xl">
                    <h4 class="font-bold text-cyan-400 border-b border-white/5 pb-1 mb-1 flex items-center justify-between">
                        <span>실시간 물리 예측</span>
                        <i class="fa-solid fa-calculator text-[9px]"></i>
                    </h4>
                    <div class="flex justify-between">
                        <span>비행 시간 (t):</span>
                        <span id="pred-t" class="font-mono text-white font-bold">0.00 s</span>
                    </div>
                    <div class="flex justify-between">
                        <span>수평 거리 (x):</span>
                        <span id="pred-x" class="font-mono text-white font-bold">0.00 m</span>
                    </div>
                    <div class="flex justify-between">
                        <span>최고 높이 (y_max):</span>
                        <span id="pred-y" class="font-mono text-white font-bold">0.00 m</span>
                    </div>
                </div>
            </div>

            <!-- 하단 물리 변수 미세조정 조종 보드 -->
            <div class="glass rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
                <!-- 속도 조절 -->
                <div class="md:col-span-4 space-y-1.5">
                    <div class="flex justify-between items-center">
                        <label class="text-[11px] text-slate-400 font-bold flex items-center gap-1.5">
                            <span class="w-2 h-2 bg-cyan-500 rounded-full"></span>
                            초기 속도 (v₀)
                        </label>
                        <span class="text-xs text-cyan-400 font-mono font-bold"><span id="v0-val">12.0</span> m/s</span>
                    </div>
                    <input type="range" id="v0-slider" min="1" max="25" step="0.1" value="12.0" class="w-full h-1 bg-slate-800 rounded appearance-none cursor-pointer">
                </div>

                <!-- 각도 조절 -->
                <div class="md:col-span-4 space-y-1.5">
                    <div class="flex justify-between items-center">
                        <label class="text-[11px] text-slate-400 font-bold flex items-center gap-1.5">
                            <span class="w-2 h-2 bg-emerald-500 rounded-full"></span>
                            투사 각도 (θ)
                        </label>
                        <span class="text-xs text-emerald-400 font-mono font-bold"><span id="theta-val">30</span>°</span>
                    </div>
                    <input type="range" id="theta-slider" min="0" max="90" step="1" value="30" class="w-full h-1 bg-slate-800 rounded appearance-none cursor-pointer">
                </div>

                <!-- 높이 조절 -->
                <div class="md:col-span-2 space-y-1.5">
                    <div class="flex justify-between items-center">
                        <label class="text-[11px] text-slate-400 font-bold flex items-center gap-1.5">
                            <span class="w-2 h-2 bg-pink-500 rounded-full"></span>
                            발사 높이 (h)
                        </label>
                        <span class="text-xs text-pink-400 font-mono font-bold" id="h-val">3.0m</span>
                    </div>
                    <input type="range" id="h-slider" min="0" max="8" step="0.1" value="3.0" class="w-full h-1 bg-slate-800 rounded appearance-none cursor-pointer">
                </div>

                <!-- 투사 실행 물리 버튼 -->
                <div class="md:col-span-2">
                    <button onclick="launchCoin()" id="btn-fire" class="w-full py-3 rounded-xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-amber-950 font-black text-xs shadow-lg active:scale-95 transition-all duration-150 flex items-center justify-center gap-1.5">
                        <i class="fa-solid fa-paper-plane"></i> 던지기
                    </button>
                </div>
            </div>
        </div>

        <!-- 오른쪽: 타겟 세부 미션 목표 및 실험 데이터 축적 로그 (1개 열 차지) -->
        <div class="flex flex-col gap-4 h-full">
            <!-- 미션 요구서 -->
            <div class="glass rounded-2xl p-4 border border-slate-800 space-y-3">
                <h3 class="text-[11px] font-black text-cyan-400 uppercase tracking-widest flex items-center gap-2">
                    <i class="fa-solid fa-bullseye text-rose-500 text-xs"></i> 미션 가이드라인
                </h3>
                <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800 space-y-2 text-xs">
                    <div class="flex justify-between">
                        <span class="text-slate-400">목표 분수대 거리:</span>
                        <span class="font-bold text-white"><span id="target-dist">15.0</span> m</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-400">분수 구경 너비:</span>
                        <span class="font-bold text-white"><span id="target-width">2.0</span> m</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-400">성공 허용 오차:</span>
                        <span class="font-bold text-cyan-400">±<span id="target-tolerance">1.0</span> m</span>
                    </div>
                </div>
            </div>

            <!-- 실시간 누적 실험 데이터 로그 기록 보드 -->
            <div class="glass rounded-2xl p-4 border border-slate-800 flex-grow flex flex-col justify-between space-y-3 min-h-0 overflow-hidden">
                <div class="flex justify-between items-center border-b border-slate-800/80 pb-1.5">
                    <h3 class="text-[11px] font-black text-slate-300 flex items-center gap-1.5">
                        <i class="fa-solid fa-database text-cyan-400"></i> 실시간 실험 기록
                    </h3>
                    <button onclick="clearLogs()" class="text-[9px] text-slate-500 hover:text-slate-300 transition">모두 리셋</button>
                </div>
                
                <!-- 스크롤 가능한 로그 테이블 바디 -->
                <div id="log-container" class="flex-grow overflow-y-auto space-y-1 text-[10px] font-mono">
                    <div class="text-slate-500 italic text-center py-10">실행된 시뮬레이션 로그가 없습니다.</div>
                </div>

                <div class="bg-cyan-950/20 border border-cyan-800/40 rounded-xl p-2.5 text-[10px] text-cyan-300">
                    <i class="fa-solid fa-circle-info mr-1"></i> 수평 성분은 공기 저항이 없을 때 외력이 없는 등속도 직선 상태이며, 수직 성분은 가속도 $g$의 지배를 받는 독립적인 낙하 운동입니다.
                </div>
            </div>
        </div>
    </main>

    <!-- 골인 여부 성공/실패 시각 판정 안내 모달 -->
    <div id="result-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-4 hidden">
        <div class="glass rounded-3xl p-6 max-w-sm w-full border border-slate-800 shadow-2xl text-center space-y-5 relative overflow-hidden">
            <div id="result-glow" class="absolute -top-24 left-1/2 -translate-x-1/2 w-48 h-48 rounded-full blur-3xl opacity-50"></div>
            
            <div class="space-y-1 relative z-10">
                <span id="result-badge" class="px-2.5 py-0.5 rounded-full text-[10px] font-black uppercase tracking-widest">SUCCESS</span>
                <h2 id="result-title" class="text-2xl font-black text-white">골인 성공! 🎉</h2>
                <p id="result-msg" class="text-slate-400 text-xs">최적의 발사 궤적을 명중시켰습니다.</p>
            </div>

            <!-- 물리 데이터 상세 전광판 -->
            <div class="bg-slate-900/60 rounded-2xl p-3.5 border border-slate-800 grid grid-cols-2 gap-3 text-left font-mono text-[11px]">
                <div>
                    <span class="text-slate-400 text-[10px]">초기 속도 (v₀)</span>
                    <div class="text-white font-bold"><span id="res-v0">12.0</span> m/s</div>
                </div>
                <div>
                    <span class="text-slate-400 text-[10px]">발사 각도 (θ)</span>
                    <div class="text-white font-bold"><span id="res-theta">30</span>°</div>
                </div>
                <div>
                    <span class="text-slate-400 text-[10px]">비행 시간 (t)</span>
                    <div class="text-cyan-400 font-bold"><span id="res-t">1.25</span> s</div>
                </div>
                <div>
                    <span class="text-slate-400 text-[10px]">낙하 거리 (x)</span>
                    <div class="text-amber-400 font-bold"><span id="res-x">15.20</span> m</div>
                </div>
                <div class="col-span-2 border-t border-slate-800 pt-2 flex justify-between items-center text-[10px]">
                    <span class="text-slate-400">목표와의 수평 오차(Δx):</span>
                    <span id="res-error" class="text-emerald-400 font-bold">0.00 m</span>
                </div>
            </div>

            <!-- 피드백 섹션 -->
            <div class="bg-slate-950/60 p-3 rounded-xl text-left border border-slate-800 text-[10px] leading-relaxed text-slate-300" id="result-tip"></div>

            <div class="flex gap-2">
                <button onclick="closeModal(false)" class="flex-grow py-2.5 rounded-xl glass hover:bg-slate-800 text-slate-300 text-xs font-bold transition">다시 시도</button>
                <button onclick="closeModal(true)" class="flex-grow py-2.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white text-xs font-bold transition">다음 단계</button>
            </div>
        </div>
    </div>

    <!-- 핵심 물리 수치 렌더링용 자바스크립트 소스코드 -->
    <script>
        // --- 전역 변수 설정 ---
        let level = 1;
        let score = 0;
        let bestScore = 0;
        
        let g_accel = 9.80;
        let air_drag_k = 0.00;
        let windFactor = 0.0;
        
        let targetX = 14.0;
        let targetWidth = 2.0;
        let targetTolerance = 1.0;

        let coin = {
            active: false,
            x: 0, y: 0,
            vx: 0, vy: 0,
            t: 0,
            spinAngle: 0,
            trail: []
        };

        let particles = []; // 물보라 효과 저장소

        let canvas, ctx;
        const originPx = { x: 70, y: 290 }; // 좌표 기준원점 패딩 값
        const pxPerMeter = 18; // 1m 당 화면 픽셀 비율

        window.onload = function() {
            canvas = document.getElementById('physics-canvas');
            ctx = canvas.getContext('2d');
            
            resizeCanvas();
            window.addEventListener('resize', () => {
                resizeCanvas();
                drawScene();
            });

            // 최고점 복구 로드
            const savedBest = localStorage.getItem('fountain_best_score');
            if(savedBest) {
                bestScore = parseInt(savedBest);
                document.getElementById('best-score').innerText = bestScore;
            }

            setupControls();
            initLevel();
            updatePredictions();

            // 프레임 애니메이션 루프 가속화
            requestAnimationFrame(simulationLoop);
        };

        function resizeCanvas() {
            const parent = canvas.parentNode;
            canvas.width = parent.clientWidth;
            canvas.height = parent.clientHeight;
        }

        function setupControls() {
            const vS = document.getElementById('v0-slider');
            const thS = document.getElementById('theta-slider');
            const hS = document.getElementById('h-slider');

            vS.addEventListener('input', (e) => {
                document.getElementById('v0-val').innerText = parseFloat(e.target.value).toFixed(1);
                updatePredictions();
                drawScene();
            });
            thS.addEventListener('input', (e) => {
                document.getElementById('theta-val').innerText = e.target.value;
                updatePredictions();
                drawScene();
            });
            hS.addEventListener('input', (e) => {
                document.getElementById('h-val').innerText = parseFloat(e.target.value).toFixed(1) + 'm';
                updatePredictions();
                drawScene();
            });
        }

        // --- 레벨 및 지형 조건 로드 ---
        function initLevel() {
            targetX = 10.0 + (level * 2.8); // 단계별 사거리 변화
            targetWidth = Math.max(1.1, 2.5 - (level * 0.2)); // 그릇 좁아짐
            
            if(level >= 3) {
                windFactor = (Math.random() * 3.5 - 1.75); // 역풍 및 순풍 생성
                document.getElementById('wind-badge').classList.remove('hidden');
                document.getElementById('wind-text').innerText = `${windFactor >= 0 ? '▶ ' : '◀ '}${Math.abs(windFactor).toFixed(2)} m/s²`;
            } else {
                windFactor = 0.0;
                document.getElementById('wind-badge').classList.add('hidden');
            }

            document.getElementById('game-level').innerText = "Level " + level;
            document.getElementById('target-dist').innerText = targetX.toFixed(1);
            document.getElementById('target-width').innerText = targetWidth.toFixed(1);
            document.getElementById('target-tolerance').innerText = targetTolerance.toFixed(1);

            coin.active = false;
            updatePredictions();
            drawScene();
        }

        // --- 궤적 해석 수학 엔진 ---
        function updatePredictions() {
            const v0 = parseFloat(document.getElementById('v0-slider').value);
            const theta = parseFloat(document.getElementById('theta-slider').value) * Math.PI / 180;
            const h = parseFloat(document.getElementById('h-slider').value);

            const vx0 = v0 * Math.cos(theta);
            const vy0 = v0 * Math.sin(theta);

            // 포물선 정량해 공식 판별식 적용
            const a = 0.5 * g_accel;
            const b = -vy0;
            const c = -h;

            let t_flight = 0;
            if(a > 0) {
                const disc = b*b - 4*a*c;
                if(disc >= 0) t_flight = (-b + Math.sqrt(disc)) / (2*a);
            }

            const x_range = vx0 * t_flight;
            const peak_y = h + (vy0 > 0 ? (vy0 * vy0) / (2 * g_accel) : 0);

            document.getElementById('pred-t').innerText = t_flight.toFixed(2) + ' s';
            document.getElementById('pred-x').innerText = x_range.toFixed(2) + ' m';
            document.getElementById('pred-y').innerText = peak_y.toFixed(2) + ' m';
        }

        // --- 동전 론처 트리거 ---
        function launchCoin() {
            if(coin.active) return;

            const v0 = parseFloat(document.getElementById('v0-slider').value);
            const theta = parseFloat(document.getElementById('theta-slider').value) * Math.PI / 180;
            const h = parseFloat(document.getElementById('h-slider').value);

            coin.x = 0;
            coin.y = h;
            coin.vx = v0 * Math.cos(theta);
            coin.vy = v0 * Math.sin(theta);
            coin.t = 0;
            coin.spinAngle = 0;
            coin.trail = [];
            coin.active = true;

            document.getElementById('btn-fire').disabled = true;
            document.getElementById('btn-fire').classList.add('opacity-40');
        }

        // --- 실시간 물리 제어 루프 ---
        function simulationLoop() {
            updatePhysics();
            drawScene();
            requestAnimationFrame(simulationLoop);
        }

        function updatePhysics() {
            // 물보라 입자 역학 프레임 갱신
            for(let i=particles.length-1; i>=0; i--) {
                const p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.vy += 0.25; // 입자용 간이 중력 작용
                p.alpha -= 0.02;
                if(p.alpha <= 0) particles.splice(i, 1);
            }

            if(!coin.active) return;

            const dt = 0.018; // 수치 연산 시간 간격 단위
            coin.t += dt;
            coin.spinAngle += 0.15; // 자전 회전 효과 증분

            coin.trail.push({ x: coin.x, y: coin.y });
            if(coin.trail.length > 40) coin.trail.shift();

            // 외력 방정식 적용
            const ax = -air_drag_k * coin.vx + windFactor;
            const ay = -g_accel - air_drag_k * coin.vy;

            coin.vx += ax * dt;
            coin.vy += ay * dt;
            coin.x += coin.vx * dt;
            coin.y += coin.vy * dt;

            // 지면 충돌 체크
            if(coin.y <= 0) {
                coin.y = 0;
                coin.active = false;
                spawnWaterSplash(coin.x); // 물보라 분출
                setTimeout(evaluateSimulation, 650); // 살짝 딜레이 후 모달 창 호출
            }
        }

        // 물줄기 분출 연출
        function spawnWaterSplash(impactX) {
            const isSuccess = Math.abs(impactX - targetX) <= (targetWidth / 2);
            const color = isSuccess ? '#22d3ee' : '#e2e8f0'; // 성공 시 시원한 청록색 물, 실패 시 흙먼지색
            
            for(let i=0; i<25; i++) {
                particles.push({
                    x: originPx.x + (impactX * pxPerMeter),
                    y: originPx.y,
                    vx: (Math.random() * 4 - 2),
                    vy: -(Math.random() * 6 + 3),
                    alpha: 1.0,
                    color: color
                });
            }
        }

        // --- 결과 종합 채점 판정기 ---
        function evaluateSimulation() {
            document.getElementById('btn-fire').disabled = false;
            document.getElementById('btn-fire').classList.remove('opacity-40');

            const error = coin.x - targetX;
            const isSuccess = Math.abs(error) <= (targetWidth / 2);

            // 데이터 통계 갱신 및 스크롤 로그 누적
            pushExperimentLog(isSuccess);

            // 전광판 데이터 바인딩
            document.getElementById('res-v0').innerText = parseFloat(document.getElementById('v0-slider').value).toFixed(1);
            document.getElementById('res-theta').innerText = document.getElementById('theta-slider').value;
            document.getElementById('res-t').innerText = coin.t.toFixed(2);
            document.getElementById('res-x').innerText = coin.x.toFixed(2);
            
            const errorBadge = document.getElementById('res-error');
            errorBadge.innerText = `${error >= 0 ? '+' : ''}${error.toFixed(2)} m`;
            errorBadge.className = isSuccess ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold';

            const badge = document.getElementById('result-badge');
            const title = document.getElementById('result-title');
            const msg = document.getElementById('result-msg');
            const glow = document.getElementById('result-glow');
            const tip = document.getElementById('result-tip');

            if(isSuccess) {
                badge.innerText = "SUCCESS";
                badge.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-950 text-emerald-400 border border-emerald-800";
                title.innerText = "골인 성공! 🎉";
                msg.innerText = "완벽한 포물선 방정식 제어로 분수대 안착에 성공했습니다.";
                glow.style.backgroundColor = "rgba(16, 185, 129, 0.4)";
                
                score += 100;
                if(score > bestScore) {
                    bestScore = score;
                    localStorage.setItem('fountain_best_score', bestScore);
                    document.getElementById('best-score').innerText = bestScore;
                }
                tip.innerText = "매우 정밀한 투사 제어였습니다! 수평 가속도 변수와 수직 하방 가속도 매트릭스를 조절하여 성공 궤적을 훌륭하게 설계하였습니다.";
            } else {
                badge.innerText = "FAILED";
                badge.className = "px-2.5 py-0.5 rounded-full text-[10px] font-black bg-rose-950 text-rose-400 border border-rose-800";
                title.innerText = "탈락했습니다!";
                msg.innerText = "낙하 한계치를 벗어나 안착에 실패했습니다.";
                glow.style.backgroundColor = "rgba(244, 63, 94, 0.4)";

                if(error < 0) {
                    tip.innerText = `분수대 중심과의 거리(${targetX.toFixed(1)}m)보다 수평 도달 거리(${coin.x.toFixed(1)}m)가 부족합니다. 발사각도를 45도 방향으로 보정하거나 투사 속력 v₀를 높여 수평 도달량을 증가시키세요.`;
                } else {
                    tip.innerText = `투사체가 분수대 목표를 초과해 날아갔습니다(${coin.x.toFixed(1)}m). 발사 기하 고도를 낮추거나, 각도를 수정하고 발사 속력을 소폭 감속해 주십시오.`;
                }
            }

            document.getElementById('result-modal').classList.remove('hidden');
        }

        function closeModal(advance) {
            document.getElementById('result-modal').classList.add('hidden');
            if(advance && score > 0) {
                level++;
            }
            initLevel();
        }

        // --- 실험 데이터 기록 ---
        function pushExperimentLog(isSuccess) {
            const container = document.getElementById('log-container');
            if(container.innerHTML.includes('실행된 시뮬레이션 로그가 없습니다.')) {
                container.innerHTML = '';
            }

            const v0 = document.getElementById('v0-slider').value;
            const theta = document.getElementById('theta-slider').value;
            const h = document.getElementById('h-slider').value;

            const logItem = document.createElement('div');
            logItem.className = `p-2 rounded border transition-colors ${isSuccess ? 'bg-emerald-950/20 border-emerald-900/40 text-emerald-300' : 'bg-slate-900 border-slate-800 text-slate-400'}`;
            logItem.innerHTML = `
                <div class="flex justify-between items-center">
                    <span><b>v₀</b>:${v0}m/s | <b>θ</b>:${theta}° | <b>h</b>:${h}m</span>
                    <span><b>x_도달</b>: ${coin.x.toFixed(2)}m (${isSuccess ? '골인' : '탈락'})</span>
                </div>
            `;
            container.prepend(logItem);
        }

        function clearLogs() {
            document.getElementById('log-container').innerHTML = '<div class="text-slate-500 italic text-center py-10">실행된 시뮬레이션 로그가 없습니다.</div>';
        }

        // --- 캔버스 그래픽 비주얼 처리 엔진 ---
        function drawScene() {
            if(!ctx) return;
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const v0 = parseFloat(document.getElementById('v0-slider').value);
            const theta = parseFloat(document.getElementById('theta-slider').value) * Math.PI / 180;
            const h = parseFloat(document.getElementById('h-slider').value);

            // 1. 그라운드 바닥면 배치
            ctx.strokeStyle = '#1e293b';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(0, originPx.y);
            ctx.lineTo(canvas.width, originPx.y);
            ctx.stroke();

            // 그라운드 지하 채우기 패턴
            ctx.fillStyle = '#0a0d16';
            ctx.fillRect(0, originPx.y + 2, canvas.width, canvas.height - originPx.y);

            // 2. 다단식 석조 분수대 (Classical Fountain) 정밀 드로잉
            const targetCenterPx = originPx.x + (targetX * pxPerMeter);
            const targetWidthPx = targetWidth * pxPerMeter;
            const baseLeft = targetCenterPx - targetWidthPx/2;

            // [석조 분수대 1단 바닥 기둥]
            ctx.fillStyle = '#334155';
            ctx.strokeStyle = '#475569';
            ctx.lineWidth = 1.5;
            ctx.fillRect(targetCenterPx - 30, originPx.y - 12, 60, 12);
            ctx.strokeRect(targetCenterPx - 30, originPx.y - 12, 60, 12);

            // [석조 분수대 2단 원형 석조 구조물]
            ctx.beginPath();
            ctx.ellipse(targetCenterPx, originPx.y - 12, targetWidthPx/2, 10, 0, 0, 2 * Math.PI);
            ctx.fillStyle = '#475569';
            ctx.fill();
            ctx.stroke();

            // [물 차오름 내부 수면 드로잉]
            ctx.fillStyle = 'rgba(6, 182, 212, 0.4)';
            ctx.beginPath();
            ctx.ellipse(targetCenterPx, originPx.y - 14, targetWidthPx/2.05, 8, 0, 0, 2 * Math.PI);
            ctx.fill();

            // [분수대 중앙 3단 높이 솟구치는 돌기둥]
            ctx.fillStyle = '#334155';
            ctx.fillRect(targetCenterPx - 8, originPx.y - 45, 16, 33);
            ctx.strokeRect(targetCenterPx - 8, originPx.y - 45, 16, 33);

            // [뿜어 나오는 역동적 물줄기 연출]
            const seconds = Date.now() / 1000;
            ctx.strokeStyle = 'rgba(34, 211, 238, 0.6)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            // 물벼락 좌우 분출 곡선식 그리기
            ctx.arc(targetCenterPx, originPx.y - 45, 20 + Math.sin(seconds*4)*2, Math.PI, 0);
            ctx.stroke();

            // 3. 발사대 거치대 및 캐논 포대 렌더링
            const launchH_px = h * pxPerMeter;
            ctx.fillStyle = '#1e293b';
            ctx.fillRect(originPx.x - 20, originPx.y - launchH_px, 25, launchH_px);
            ctx.strokeStyle = '#334155';
            ctx.lineWidth = 1.5;
            ctx.strokeRect(originPx.x - 20, originPx.y - launchH_px, 25, launchH_px);

            // 회전 포신 드로잉
            ctx.save();
            ctx.translate(originPx.x - 7, originPx.y - launchH_px);
            ctx.rotate(-theta);
            ctx.fillStyle = '#475569';
            ctx.fillRect(0, -5, 20, 10);
            ctx.strokeStyle = '#64748b';
            ctx.strokeRect(0, -5, 20, 10);
            ctx.restore();

            // x=0m 기준선 가이드 텍스트
            ctx.fillStyle = '#475569';
            ctx.font = '8px monospace';
            ctx.fillText('x=0m', originPx.x - 12, originPx.y + 14);

            // 4. 발사 이전 점선 가이드 궤적 표시
            if(!coin.active) {
                drawPreviewPath(v0, theta, h);
            }

            // 5. 입자 물리 물보라 그리기
            for(let p of particles) {
                ctx.fillStyle = p.color;
                ctx.globalAlpha = p.alpha;
                ctx.beginPath();
                ctx.arc(p.x, p.y, 2.5, 0, Math.PI*2);
                ctx.fill();
            }
            ctx.globalAlpha = 1.0; // 복귀

            // 6. 비행 중인 실제 입체 회전 동전 그리기 (Specular Coin Design)
            if(coin.active) {
                // 선행 잔상 궤적 드로잉
                if(coin.trail.length > 1) {
                    ctx.beginPath();
                    ctx.strokeStyle = 'rgba(245, 158, 11, 0.4)';
                    ctx.lineWidth = 3;
                    const st = getCanvasCoords(coin.trail[0].x, coin.trail[0].y);
                    ctx.moveTo(st.x, st.y);
                    for(let i=1; i<coin.trail.length; i++) {
                        const pt = getCanvasCoords(coin.trail[i].x, coin.trail[i].y);
                        ctx.lineTo(pt.x, pt.y);
                    }
                    ctx.stroke();
                }

                // 회전축 적용 동전 바디
                const coinPos = getCanvasCoords(coin.x, coin.y);
                ctx.save();
                ctx.translate(coinPos.x, coinPos.y);
                // 비행 시간에 비례한 공중 회전률 적용
                ctx.scale(Math.abs(Math.sin(coin.spinAngle)), 1.0);

                // 금빛 황동 동전 그라데이션 몸체
                ctx.beginPath();
                ctx.arc(0, 0, 7.5, 0, Math.PI * 2);
                ctx.fillStyle = '#d97706';
                ctx.fill();

                ctx.beginPath();
                ctx.arc(0, 0, 6, 0, Math.PI * 2);
                ctx.fillStyle = '#fbbf24';
                ctx.fill();

                // '₩' 음각 문자 기호 가공 배치
                ctx.fillStyle = '#78350f';
                ctx.font = 'black 8px Arial';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('₩', 0, 0);

                ctx.restore();
            }
        }

        // 실시간 점선 물리 가이드 미리보기 계산식
        function drawPreviewPath(v0, theta, h) {
            ctx.beginPath();
            ctx.setLineDash([3, 4]);
            ctx.strokeStyle = 'rgba(148, 163, 184, 0.35)';
            ctx.lineWidth = 1.2;

            let testX = 0;
            let testY = h;
            let vx = v0 * Math.cos(theta);
            let vy = v0 * Math.sin(theta);
            const dt = 0.05;

            const st = getCanvasCoords(testX, testY);
            ctx.moveTo(st.x, st.y);

            for(let t=0; t<4; t+=dt) {
                // 이산 미적 오차 보정을 고려한 가이드라인 계산
                const ax = -air_drag_k * vx + windFactor;
                const ay = -g_accel - air_drag_k * vy;
                
                vx += ax * dt;
                vy += ay * dt;
                testX += vx * dt;
                testY += vy * dt;

                const pt = getCanvasCoords(testX, testY);
                ctx.lineTo(pt.x, pt.y);
                
                if(testY < 0) break;
            }
            ctx.stroke();
            ctx.setLineDash([]); // 대시 상태 복구
        }

        // 캔버스 좌표 매핑용 헬퍼 함수
        function getCanvasCoords(mX, mY) {
            return {
                x: originPx.x + (mX * pxPerMeter),
                y: originPx.y - (mY * pxPerMeter)
            };
        }
    </script>
</body>
</html>
"""

# 4. Streamlit 메인 콘텐츠 화면 구성
st.title("🪙 분수대에 동전 던지기 - 물리 시뮬레이터 배포")
st.caption("30806 김성준 - 물리학 2 과제 수행 및 시뮬레이터 실시간 구동기")

st.info("💡 초기 속도, 발사각도, 거치 고도를 정밀하게 제어하여 대리석 석조 분수대에 금빛 동전을 명중시키십시오! 수집된 물리 실험 데이터는 실시간 통계 보드에 축적됩니다.")

# 5. HTML 컴포넌트를 반응형으로 삽입
components.html(html_code, height=600, scrolling=True)
