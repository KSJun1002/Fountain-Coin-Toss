import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 설정 (전체 화면 모드 및 전용 타이틀 설정)
st.set_page_config(
    page_title="Fountain Coin Toss - 물리학 주제탐구 시뮬레이터",
    page_icon="🪙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 웹 브라우저 스타일링 및 마진 최소화 (제목 글자 잘림 현상 완화 스타일 추가)
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
            padding-left: 1.5rem;
            padding-right: 1.5rem;
        }
        /* 메인 제목(h1) 한글 자모음 하단부 잘림 문제 완벽 해결 */
        h1 {
            line-height: 1.4 !important;
            padding-bottom: 12px !important;
            overflow: visible !important;
        }
        iframe {
            border-radius: 16px;
            box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.4), 0 10px 15px -10px rgba(0, 0, 0, 0.4);
        }
    </style>
""", unsafe_allow_html=True)

# 3. 홈 화면, 게임 인터페이스, 물리학 3단 학습모드, 설정창이 완벽하게 결합된 원본 HTML5 엔진 코드
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fountain Coin Toss - 분수대에 동전 넣기</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght=300;400;500;700;900&display=swap');
        body {
            font-family: 'Noto Sans KR', sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            overflow-x: hidden;
        }
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #1e293b;
        }
        ::-webkit-scrollbar-thumb {
            background: #475569;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #64748b;
        }
        /* Glassmorphism utility */
        .glass {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-bright {
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        /* Water fountain animation */
        @keyframes waterFlow {
            0% { transform: translateY(0) scaleY(1); opacity: 0.8; }
            50% { transform: translateY(-10px) scaleY(1.1); opacity: 1; }
            100% { transform: translateY(0) scaleY(1); opacity: 0.8; }
        }
        .water-splash {
            animation: waterFlow 2s infinite ease-in-out;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between">

    <!-- Top Navigation Header -->
    <header class="glass sticky top-0 z-50 px-6 py-4 flex justify-between items-center border-b border-slate-800">
        <div class="flex items-center gap-3 cursor-pointer" onclick="goHome()">
            <div class="bg-gradient-to-tr from-cyan-500 to-blue-600 p-2.5 rounded-xl shadow-lg shadow-cyan-500/20">
                <i class="fa-solid fa-coins text-white text-xl"></i>
            </div>
            <div>
                <span class="text-xs text-cyan-400 font-bold uppercase tracking-wider block">Physics Simulator</span>
                <h1 class="text-lg font-black tracking-tight text-white">Fountain Coin Toss</h1>
            </div>
        </div>
        <div class="flex gap-2">
            <button onclick="goHome()" class="px-4 py-2 rounded-lg text-sm font-semibold text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200">
                <i class="fa-solid fa-house mr-1.5"></i> 홈
            </button>
            <button onclick="goLearn()" class="px-4 py-2 rounded-lg text-sm font-semibold text-slate-300 hover:text-white hover:bg-slate-800 transition duration-200">
                <i class="fa-solid fa-graduation-cap mr-1.5"></i> 학습 모드
            </button>
            <button onclick="openSettings()" class="p-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition">
                <i class="fa-solid fa-sliders text-lg"></i>
            </button>
        </div>
    </header>

    <!-- Main Workspace Container -->
    <main class="flex-grow max-w-7xl w-full mx-auto p-4 md:p-6 flex flex-col justify-center items-center">

        <!-- ① START SCREEN (HOME) -->
        <section id="home-screen" class="w-full max-w-4xl py-12 flex flex-col items-center justify-center text-center space-y-8 animate-fadeIn">
            <!-- Decorative 3-Tier Marble Fountain Animation Graphic -->
            <div class="relative w-64 h-64 flex items-end justify-center mb-4">
                <!-- Sky backdrop -->
                <div class="absolute inset-0 bg-gradient-to-b from-blue-950/40 to-cyan-950/20 rounded-full blur-2xl"></div>
                
                <!-- 3-Tier Marble Fountain Base Structure -->
                <div class="relative z-10 flex flex-col items-center">
                    <!-- Top Bowl (3단 소형 보울) -->
                    <div class="w-16 h-3.5 bg-gradient-to-r from-slate-600 via-slate-300 to-slate-800 rounded-full border border-slate-500 shadow-md"></div>
                    <!-- Top Stem (상부 기둥) -->
                    <div class="w-4 h-6 bg-gradient-to-r from-slate-700 via-slate-400 to-slate-900 border-x border-slate-600 shadow-inner"></div>
                    <!-- Middle Bowl (2단 중간 보울) -->
                    <div class="w-32 h-6 bg-gradient-to-r from-slate-600 via-slate-400 to-slate-800 rounded-full border border-slate-500 shadow-lg flex items-center justify-center relative">
                        <!-- Water surface ripple -->
                        <div class="absolute inset-1 bg-cyan-500/30 rounded-full blur-[1px] animate-pulse"></div>
                    </div>
                    <!-- Bottom Pedestal (하부 받침대) -->
                    <div class="w-8 h-10 bg-gradient-to-r from-slate-700 via-slate-500 to-slate-900 border-x border-slate-600 shadow-inner"></div>
                    <!-- Bottom Base Pool (1단 가장 큰 대형 수조) -->
                    <div class="w-48 h-10 bg-gradient-to-r from-slate-800 via-slate-600 to-slate-950 rounded-t-full border-t border-slate-500 shadow-xl flex items-center justify-center overflow-hidden relative">
                        <!-- Water pool effect -->
                        <div class="absolute inset-x-0 bottom-0 h-4 bg-cyan-500/40 blur-[1px]"></div>
                    </div>
                </div>

                <!-- Animated Water Sprays SVG -->
                <svg class="absolute bottom-10 left-1/2 -translate-x-1/2 w-56 h-48 pointer-events-none" viewBox="0 0 100 80">
                    <!-- Top bowl splashes spilling to Mid bowl -->
                    <path class="water-splash fill-none stroke-cyan-400/80 stroke-[2] stroke-dasharray-[3,1.5]" d="M 50,22 Q 35,-2 25,25" />
                    <path class="water-splash fill-none stroke-cyan-400/80 stroke-[2]" d="M 50,22 Q 65,-2 75,25" style="animation-delay: 0.5s;" />
                    <!-- Center main spout -->
                    <path class="water-splash fill-none stroke-cyan-300 stroke-[3]" d="M 50,20 Q 50,-8 50,20" style="animation-delay: 1s;" />
                    <!-- Mid bowl spilling water to bottom base -->
                    <path class="water-splash fill-none stroke-cyan-500/60 stroke-[1.5]" d="M 34,35 Q 20,45 15,70" style="animation-delay: 0.3s;" />
                    <path class="water-splash fill-none stroke-cyan-500/60 stroke-[1.5]" d="M 66,35 Q 80,45 85,70" style="animation-delay: 0.8s;" />
                </svg>

                <!-- Flying Coin Arc -->
                <div class="absolute top-12 left-4 w-6 h-6 bg-amber-400 rounded-full border-2 border-amber-300 shadow-lg shadow-amber-400/50 flex items-center justify-center animate-bounce">
                    <span class="text-[8px] font-bold text-amber-900">₩</span>
                </div>
            </div>

            <div class="space-y-3">
                <h2 class="text-4xl md:text-5xl font-black tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white via-slate-100 to-cyan-400">
                    분수대에 동전 던지기
                </h2>
                <p class="text-slate-400 max-w-md mx-auto text-sm md:text-base">
                    초기 발사 속도와 발사 각도를 조절해 수평 투사 운동과 포물선 운동의 물리학적 원리를 학습하며 동전을 분수대에 넣어 보세요!
                </p>
            </div>

            <!-- Dashboard Stats -->
            <div class="grid grid-cols-2 gap-4 w-full max-w-sm">
                <div class="glass rounded-xl p-3 text-center">
                    <span class="text-xs text-slate-400 block">최고 점수 (Best)</span>
                    <span id="best-score-display" class="text-xl font-black text-yellow-400">0 점</span>
                </div>
                <div class="glass rounded-xl p-3 text-center">
                    <span class="text-xs text-slate-400 block">진행 레벨</span>
                    <span id="current-level-display" class="text-xl font-black text-cyan-400">Level 1</span>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-4 w-full max-w-md">
                <button onclick="startGame()" class="flex-1 py-4 px-6 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold text-lg shadow-lg shadow-cyan-500/20 active:scale-95 transition duration-150 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-play"></i> 게임 시작하기
                </button>
                <button onclick="goLearn()" class="flex-1 py-4 px-6 rounded-xl glass hover:bg-slate-800 text-white font-bold text-lg border border-slate-700 active:scale-95 transition duration-150 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-graduation-cap"></i> 물리 학습 모드
                </button>
            </div>
        </section>

        <!-- ② GAME PLAY SCREEN -->
        <section id="game-screen" class="w-full hidden grid grid-cols-1 lg:grid-cols-3 gap-6 animate-fadeIn">
            
            <!-- Left & Middle: Main Physics Arena & Controls (2 cols) -->
            <div class="lg:col-span-2 flex flex-col gap-4">
                
                <!-- Game Info Bar -->
                <div class="glass rounded-2xl p-4 flex justify-between items-center border border-slate-800">
                    <div class="flex items-center gap-4">
                        <span class="bg-cyan-950/50 border border-cyan-800 text-cyan-400 px-3 py-1.5 rounded-xl font-bold text-sm">
                            Level <span id="game-level">1</span>
                        </span>
                        <div class="flex items-center gap-1.5">
                            <span class="text-slate-400 text-xs font-semibold">잔여 동전:</span>
                            <div id="lives-container" class="flex gap-1">
                                <!-- Will be drawn by JS (coin icons) -->
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center gap-6">
                        <div>
                            <span class="text-slate-400 text-xs font-semibold mr-1">점수:</span>
                            <span id="game-score" class="font-black text-xl text-yellow-400">0</span>
                        </div>
                        <button onclick="togglePause()" id="btn-pause" class="text-slate-400 hover:text-white transition">
                            <i class="fa-solid fa-pause text-lg"></i>
                        </button>
                    </div>
                </div>

                <!-- Simulation View Area -->
                <div class="relative glass rounded-2xl border border-slate-800 overflow-hidden h-96 w-full flex flex-col justify-between">
                    <!-- Environment Background Sky to Ground -->
                    <div class="absolute inset-0 bg-gradient-to-b from-slate-950 via-slate-900 to-cyan-950/20 -z-10"></div>
                    
                    <!-- Wind indicator (for higher levels) -->
                    <div id="wind-indicator" class="absolute top-4 right-4 bg-slate-950/70 border border-slate-800 text-slate-300 rounded-lg px-3 py-1.5 text-xs flex items-center gap-2 z-10 hidden">
                        <i class="fa-solid fa-wind text-cyan-400"></i>
                        <span>바람: <b id="wind-value" class="text-cyan-400">0.0 m/s</b></span>
                    </div>

                    <!-- Target / Launcher Coordinates overlay -->
                    <div class="absolute top-4 left-4 text-[10px] text-slate-500 font-mono space-y-0.5 pointer-events-none z-10">
                        <div>중력 가속도(g) = <span id="env-g">9.8</span> m/s²</div>
                        <div>공기저항(k) = <span id="env-k">0.0</span></div>
                    </div>

                    <!-- Canvas for physics visualization -->
                    <canvas id="physics-canvas" class="w-full h-full cursor-crosshair"></canvas>
                    
                    <!-- Trajectory Overlay Info Box -->
                    <div class="absolute bottom-4 right-4 glass-bright rounded-xl p-3 text-xs space-y-1 text-slate-300 pointer-events-none w-48 border border-white/10">
                        <h4 class="font-bold text-cyan-400 border-b border-white/10 pb-1 mb-1.5 flex items-center justify-between">
                            <span>실시간 물리 예측</span>
                            <i class="fa-solid fa-calculator"></i>
                        </h4>
                        <div class="flex justify-between">
                            <span>예측 비행시간(t):</span>
                            <span id="pred-t" class="font-mono text-white">0.00 s</span>
                        </div>
                        <div class="flex justify-between">
                            <span>수평 도달거리(x):</span>
                            <span id="pred-x" class="font-mono text-white">0.00 m</span>
                        </div>
                        <div class="flex justify-between">
                            <span>최대 상승높이(y):</span>
                            <span id="pred-y" class="font-mono text-white">0.00 m</span>
                        </div>
                    </div>
                </div>

                <!-- Game Launch Control Panel -->
                <div class="glass rounded-2xl p-5 border border-slate-800 grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
                    
                    <!-- Speed Control -->
                    <div class="md:col-span-4 space-y-2">
                        <div class="flex justify-between items-center">
                            <label class="text-xs text-slate-400 font-bold flex items-center gap-1.5">
                                <span class="w-2 h-2 bg-cyan-500 rounded-full"></span>
                                초기 속도 (v₀)
                            </label>
                            <div class="flex items-center gap-1">
                                <input type="number" id="v0-num" min="1" max="25" step="0.1" value="12.0" class="w-14 text-center bg-slate-900 border border-slate-700 rounded p-0.5 text-xs text-cyan-400 font-bold focus:outline-none focus:border-cyan-500">
                                <span class="text-[10px] text-slate-500">m/s</span>
                            </div>
                        </div>
                        <input type="range" id="v0-slider" min="1" max="25" step="0.1" value="12.0" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
                        <div class="flex justify-between text-[10px] text-slate-500">
                            <span>1 m/s</span>
                            <span>13 m/s</span>
                            <span>25 m/s</span>
                        </div>
                    </div>

                    <!-- Angle Control -->
                    <div class="md:col-span-4 space-y-2">
                        <div class="flex justify-between items-center">
                            <label class="text-xs text-slate-400 font-bold flex items-center gap-1.5">
                                <span class="w-2 h-2 bg-emerald-500 rounded-full"></span>
                                발사 각도 (θ)
                            </label>
                            <div class="flex items-center gap-1">
                                <input type="number" id="theta-num" min="0" max="90" step="1" value="30" class="w-12 text-center bg-slate-900 border border-slate-700 rounded p-0.5 text-xs text-emerald-400 font-bold focus:outline-none focus:border-emerald-500">
                                <span class="text-[10px] text-slate-500">deg</span>
                            </div>
                        </div>
                        <input type="range" id="theta-slider" min="0" max="90" step="1" value="30" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-emerald-500">
                        <div class="flex justify-between text-[10px] text-slate-500">
                            <span>0° (수평투사)</span>
                            <span>45°</span>
                            <span>90°</span>
                        </div>
                    </div>

                    <!-- Height Control -->
                    <div class="md:col-span-2 space-y-2">
                        <div class="flex justify-between items-center">
                            <label class="text-xs text-slate-400 font-bold flex items-center gap-1.5">
                                <span class="w-2 h-2 bg-pink-500 rounded-full"></span>
                                발사 높이 (h)
                            </label>
                            <span class="text-xs text-pink-400 font-bold" id="h-val">3.0m</span>
                        </div>
                        <input type="range" id="h-slider" min="1" max="8" step="0.1" value="3.0" class="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-pink-500">
                    </div>

                    <!-- Fire Button -->
                    <div class="md:col-span-2 flex flex-col justify-end h-full">
                        <button onclick="launchCoin()" id="btn-fire" class="w-full py-4 rounded-xl bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-400 hover:to-yellow-400 text-amber-950 font-black text-md shadow-lg shadow-amber-500/20 active:scale-95 transition flex items-center justify-center gap-2">
                            <i class="fa-solid fa-paper-plane"></i> 발 사
                        </button>
                    </div>
                </div>
            </div>

            <!-- Right Sidebar: Mission Info, Real-time telemetry log & Guidelines (1 col) -->
            <div class="flex flex-col gap-4">
                
                <!-- Mission Box -->
                <div class="glass rounded-2xl p-5 border border-slate-800 space-y-4">
                    <h3 class="text-sm font-black text-cyan-400 tracking-wider uppercase flex items-center gap-2">
                        <i class="fa-solid fa-bullseye text-lg text-rose-500"></i> 미션 가이드라인
                    </h3>
                    
                    <div class="bg-slate-900/50 p-3.5 rounded-xl border border-slate-800 space-y-3">
                        <div class="flex justify-between text-xs">
                            <span class="text-slate-400">목표 수평 거리 (x):</span>
                            <span class="font-bold text-white"><span id="target-dist">15.0</span> m</span>
                        </div>
                        <div class="flex justify-between text-xs">
                            <span class="text-slate-400">분수대 입구 너비:</span>
                            <span class="font-bold text-white"><span id="target-width">2.0</span> m</span>
                        </div>
                        <div class="flex justify-between text-xs">
                            <span class="text-slate-400">성공 판정 한계 오차:</span>
                            <span class="font-bold text-cyan-400">±<span id="target-tolerance">1.0</span> m</span>
                        </div>
                    </div>

                    <div class="text-xs text-slate-400 space-y-2">
                        <p class="font-semibold text-slate-300">💡 물리 힌트:</p>
                        <ul class="list-disc pl-4 space-y-1">
                            <li>발사각도가 <span class="text-emerald-400 font-semibold">0°</span>일 때는 <b>수평으로 던진 운동</b>이 됩니다.</li>
                            <li>바람이 불 때는 수평 속도가 감소하거나 증가합니다.</li>
                            <li>더 멀리 가려면 초기속도 <span class="text-cyan-400 font-semibold">v₀</span>를 키우거나 각도를 <span class="text-emerald-400 font-semibold">45°</span>에 가깝게 조절해 보세요.</li>
                        </ul>
                    </div>
                </div>

                <!-- Simulation History Real-time Telemetry Data -->
                <div class="glass rounded-2xl p-5 border border-slate-800 flex-grow flex flex-col justify-between space-y-4 min-h-[250px]">
                    <div class="flex justify-between items-center border-b border-slate-800 pb-2">
                        <h3 class="text-sm font-black text-slate-300 flex items-center gap-2">
                            <i class="fa-solid fa-list-check text-cyan-400"></i> 실험 기록 및 로그
                        </h3>
                        <button onclick="clearHistory()" class="text-[10px] text-slate-500 hover:text-slate-300 transition">기록 초기화</button>
                    </div>

                    <!-- Log Table -->
                    <div class="flex-grow overflow-y-auto max-h-[180px] text-[11px] font-mono space-y-1.5" id="history-log">
                        <div class="text-slate-500 italic text-center py-8">아직 시도한 실험이 없습니다.</div>
                    </div>

                    <div class="bg-cyan-950/20 border border-cyan-800/50 rounded-xl p-3 text-xs text-cyan-200">
                        <p class="font-semibold text-cyan-400 mb-1"><i class="fa-solid fa-circle-info mr-1"></i> 물리적 탐구과제:</p>
                        수평 거리는 $x = v_0 \cos(\theta) t$ 이고 낙하 시간 $t$는 발사 높이 $h$와 발사각 $\theta$로 결정됩니다.
                    </div>
                </div>
            </div>
        </section>

        <!-- ③ INTERACTIVE RESULTS OVERLAY MODAL -->
        <div id="result-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-4 hidden">
            <div class="glass rounded-3xl p-6 md:p-8 max-w-md w-full border border-slate-800 shadow-2xl text-center space-y-6 relative overflow-hidden">
                
                <!-- Splash background light based on success/fail -->
                <div id="result-radial-glow" class="absolute -top-24 left-1/2 -translate-x-1/2 w-48 h-48 rounded-full blur-3xl opacity-50"></div>

                <div class="space-y-2 relative z-10">
                    <span id="result-badge" class="px-3 py-1 rounded-full text-xs font-black uppercase tracking-widest">SUCCESS</span>
                    <h2 id="result-title" class="text-3xl font-black text-white">동전이 들어갔습니다! 🎉</h2>
                    <p id="result-msg" class="text-slate-400 text-sm">완벽한 각도와 물리적 계산이었습니다.</p>
                </div>

                <!-- Score Board -->
                <div class="bg-slate-900/60 rounded-2xl p-4 border border-slate-800 grid grid-cols-2 gap-4 text-left font-mono text-sm">
                    <div class="space-y-1">
                        <span class="text-slate-400 text-xs font-sans">설정 속도 (v₀)</span>
                        <div class="text-white font-bold"><span id="res-v0">12.0</span> m/s</div>
                    </div>
                    <div class="space-y-1">
                        <span class="text-slate-400 text-xs font-sans">설정 각도 (θ)</span>
                        <div class="text-white font-bold"><span id="res-theta">30</span>°</div>
                    </div>
                    <div class="space-y-1">
                        <span class="text-slate-400 text-xs font-sans">비행 시간 (t)</span>
                        <div class="text-cyan-400 font-bold"><span id="res-t">1.25</span> s</div>
                    </div>
                    <div class="space-y-1">
                        <span class="text-slate-400 text-xs font-sans">실제 낙하 거리 (x)</span>
                        <div class="text-amber-400 font-bold"><span id="res-x">15.20</span> m</div>
                    </div>
                    <div class="col-span-2 border-t border-slate-800 pt-3 flex justify-between items-center">
                        <span class="text-slate-400 font-sans text-xs">목표지점과의 수평 오차(Δx):</span>
                        <span id="res-error" class="text-rose-400 font-bold font-mono">+0.20 m</span>
                    </div>
                </div>

                <!-- Feedbacks / Hints -->
                <div class="bg-slate-950/50 p-4 rounded-xl text-left border border-slate-800">
                    <p class="text-xs font-bold text-yellow-400 mb-1"><i class="fa-solid fa-lightbulb mr-1"></i> 물리적 피드백 분석</p>
                    <p id="result-physics-tip" class="text-xs text-slate-300 leading-relaxed"></p>
                </div>

                <!-- Buttons -->
                <div class="flex gap-3 pt-2">
                    <button id="btn-result-secondary" onclick="closeResultModal(false)" class="flex-1 py-3.5 rounded-xl glass hover:bg-slate-800 text-slate-300 hover:text-white font-bold transition">
                        다시 도전 (Retry)
                    </button>
                    <button id="btn-result-primary" onclick="closeResultModal(true)" class="flex-1 py-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold transition">
                        다음 레벨 (Next Level)
                    </button>
                </div>
            </div>
        </div>

        <!-- ④ LEARNING MODE SCREEN -->
        <section id="learn-screen" class="w-full hidden space-y-6 animate-fadeIn">
            
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-800 pb-4">
                <div>
                    <h2 class="text-2xl font-black text-white flex items-center gap-2">
                        <i class="fa-solid fa-graduation-cap text-cyan-400"></i> 포물선 운동 학습 센터
                    </h2>
                    <p class="text-slate-400 text-xs md:text-sm mt-0.5">수평 투사 운동과 일반 포물선 운동의 수학적 공식 및 그래프 변화를 인터랙티브하게 체험합니다.</p>
                </div>
                
                <!-- Tab controller buttons -->
                <div class="flex bg-slate-900 border border-slate-800 rounded-xl p-1 w-full md:w-auto">
                    <button onclick="switchTab('theory')" id="tab-theory-btn" class="flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-cyan-400 bg-slate-800 shadow">
                        <i class="fa-solid fa-book-open mr-1"></i> 이론 마스터
                    </button>
                    <button onclick="switchTab('graph')" id="tab-graph-btn" class="flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-slate-400 hover:text-slate-200">
                        <i class="fa-solid fa-chart-line mr-1"></i> 실시간 그래프 탐구
                    </button>
                    <button onclick="switchTab('calculator')" id="tab-calculator-btn" class="flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-slate-400 hover:text-slate-200">
                        <i class="fa-solid fa-calculator mr-1"></i> 물리량 계산기
                    </button>
                </div>
            </div>

            <!-- Tab 1: Theory Content -->
            <div id="tab-theory" class="grid grid-cols-1 md:grid-cols-3 gap-6 animate-fadeIn">
                <!-- Physics formula & summary (2/3 width) -->
                <div class="md:col-span-2 space-y-6">
                    <div class="glass rounded-2xl p-6 border border-slate-800 space-y-4">
                        <h3 class="text-lg font-black text-white border-b border-slate-800 pb-2">1. 수평으로 던진 물체의 운동 (수평 투사)</h3>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            초기 수직 속도가 없이 수평 방향($\theta = 0^\circ$)으로만 초기 속도 $v_0$를 가지고 던져진 물체는 <b>중력</b>에 의해 하강하며 <b>포물선 경로</b>를 그리게 됩니다.
                        </p>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
                            <div class="bg-slate-900/80 rounded-xl p-4 border border-slate-800 space-y-2">
                                <span class="bg-cyan-950 text-cyan-400 text-[10px] font-black px-2 py-0.5 rounded uppercase">수평 방향 (x축)</span>
                                <p class="text-xs text-slate-400">외부의 힘이 작용하지 않으므로 <b>등속 직선 운동</b>을 합니다.</p>
                                <div class="font-mono text-white text-sm bg-slate-950 p-2 rounded text-center font-bold">
                                    $x = v_0 \cdot t$
                                </div>
                            </div>
                            <div class="bg-slate-900/80 rounded-xl p-4 border border-slate-800 space-y-2">
                                <span class="bg-rose-950 text-rose-400 text-[10px] font-black px-2 py-0.5 rounded uppercase">수직 방향 (y축)</span>
                                <p class="text-xs text-slate-400">일정한 중력 가속도($g$)의 힘을 받아 <b>자유 낙하(등가속도) 운동</b>을 합니다.</p>
                                <div class="font-mono text-white text-sm bg-slate-950 p-2 rounded text-center font-bold">
                                    $y = h - \frac{1}{2}gt^2$
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="glass rounded-2xl p-6 border border-slate-800 space-y-4">
                        <h3 class="text-lg font-black text-white border-b border-slate-800 pb-2">2. 비스듬히 던져 올린 물체의 포물선 운동</h3>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            초기 속도 $v_0$를 각도 $\theta$로 비스듬히 발사할 때의 합성 운동 공식입니다.
                        </p>
                        <div class="bg-slate-900/80 rounded-xl p-4 border border-slate-800 space-y-3 font-mono text-sm text-slate-300">
                            <div class="flex justify-between items-center border-b border-slate-800/60 pb-1.5">
                                <span>수평 위치 $x(t)$</span>
                                <span class="text-white font-bold">$x(t) = v_0 \cos(\theta) t$</span>
                            </div>
                            <div class="flex justify-between items-center border-b border-slate-800/60 pb-1.5">
                                <span>수직 위치 $y(t)$</span>
                                <span class="text-white font-bold">$y(t) = h + v_0 \sin(\theta) t - \frac{1}{2} g t^2$</span>
                            </div>
                            <div class="flex justify-between items-center border-b border-slate-800/60 pb-1.5">
                                <span>최고 높이 도달 시간 $t_{top}$</span>
                                <span class="text-cyan-400 font-bold">$t_{top} = \frac{v_0 \sin(\theta)}{g}$</span>
                            </div>
                            <div class="flex justify-between items-center">
                                <span>포물선 경로 방정식</span>
                                <span class="text-amber-400 font-bold">$y = x \tan(\theta) - \frac{g}{2 v_0^2 \cos^2(\theta)} x^2$ (단, $h=0$)</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Side Guide (1/3 width) -->
                <div class="space-y-4">
                    <div class="glass rounded-2xl p-5 border border-slate-800">
                        <h4 class="text-sm font-bold text-yellow-400 mb-2 flex items-center gap-1.5">
                            <i class="fa-solid fa-lightbulb"></i> 보고서 작성 꿀팁
                        </h4>
                        <div class="text-xs text-slate-300 space-y-2.5 leading-relaxed">
                            <p><b>[서론 목적지 설정]</b> 분수대 동전 던지기는 우리 일상의 흔한 사례이지만, 물리학 2의 다차원 운동 기술 원리를 아주 잘 드러내 줍니다. 1D 등속 운동과 1D 등가속 운동의 합성이 어떻게 하나의 2D 곡선 궤적이 되는지 증명하는 방향으로 탐구 보고서를 적어보세요.</p>
                            <p><b>[독립성의 원리]</b> 수평과 수직 방향의 운동은 상호 간섭하지 않는다는 <b>힘과 운동의 독립성</b> 원리가 핵심입니다.</p>
                        </div>
                    </div>

                    <div class="bg-gradient-to-tr from-slate-900 to-cyan-950 border border-cyan-800/40 rounded-2xl p-5 space-y-3">
                        <span class="text-[10px] text-cyan-400 font-black uppercase tracking-wider block">학습 활동 과제</span>
                        <h4 class="text-white font-bold text-sm">중력 상수를 조절하면?</h4>
                        <p class="text-xs text-slate-300 leading-relaxed">우측 상단 설정 아이콘을 눌러 <b>달의 중력 (1.6 m/s²)</b>이나 <b>목성의 중력 (24.8 m/s²)</b>으로 환경을 바꾼 후 게임을 시도해 보세요. 중력의 크기가 비행 시간과 도달 거리에 어떤 직접적 변수 관계를 갖는지 수치로 고찰할 수 있습니다.</p>
                    </div>
                </div>
            </div>

            <!-- Tab 2: Interactive Graphs -->
            <div id="tab-graph" class="hidden grid grid-cols-1 lg:grid-cols-3 gap-6 animate-fadeIn">
                <!-- Control Column (1 col) -->
                <div class="glass rounded-2xl p-5 border border-slate-800 space-y-6">
                    <h3 class="text-sm font-bold text-cyan-400 border-b border-slate-800 pb-2 flex items-center gap-1.5">
                        <i class="fa-solid fa-sliders"></i> 그래프 변수 실시간 제어
                    </h3>
                    
                    <div class="space-y-4">
                        <div class="space-y-2">
                            <div class="flex justify-between text-xs">
                                <span class="text-slate-300">초기 속도 ($v_0$)</span>
                                <span class="font-bold text-cyan-400" id="graph-v0-val">10 m/s</span>
                            </div>
                            <input type="range" id="graph-v0" min="2" max="25" step="0.5" value="10" class="w-full h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-cyan-400">
                        </div>

                        <div class="space-y-2">
                            <div class="flex justify-between text-xs">
                                <span class="text-slate-300">발사 각도 ($\theta$)</span>
                                <span class="font-bold text-emerald-400" id="graph-theta-val">45°</span>
                            </div>
                            <input type="range" id="graph-theta" min="0" max="90" step="5" value="45" class="w-full h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-emerald-400">
                        </div>

                        <div class="space-y-2">
                            <div class="flex justify-between text-xs">
                                <span class="text-slate-300">발사 높이 ($h$)</span>
                                <span class="font-bold text-pink-400" id="graph-h-val">2.0 m</span>
                            </div>
                            <input type="range" id="graph-h" min="0" max="10" step="0.5" value="2" class="w-full h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-pink-400">
                        </div>

                        <div class="space-y-2">
                            <div class="flex justify-between text-xs">
                                <span class="text-slate-300">중력 가속도 ($g$)</span>
                                <span class="font-bold text-yellow-400" id="graph-g-val">9.8 m/s²</span>
                            </div>
                            <input type="range" id="graph-g" min="1" max="25" step="0.1" value="9.8" class="w-full h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-yellow-400">
                        </div>
                    </div>

                    <div class="bg-slate-900/60 p-3.5 rounded-xl border border-slate-800 text-xs text-slate-300 space-y-1">
                        <span class="font-bold text-white block mb-1">💡 그래프 관전 포인트</span>
                        <div>1. 수평 도달 거리($x$)는 각도가 <b class="text-emerald-400">45°</b>일 때 일반적으로 최대가 됩니다.</div>
                        <div>2. <b class="text-pink-400">높이($h$)가 존재할 때</b>는 45°보다 약간 낮은 각도에서 도달 거리가 최대가 됩니다. 직접 변수를 조작하며 사실인지 검증해 보세요!</div>
                    </div>
                </div>

                <!-- Dynamic Graph Plots (2 cols) -->
                <div class="lg:col-span-2 space-y-4">
                    <div class="glass rounded-2xl p-5 border border-slate-800 flex flex-col justify-between">
                        <div class="flex justify-between items-center mb-4">
                            <span class="text-xs text-slate-400 font-bold uppercase tracking-wider block">Trajectory Chart</span>
                            <span class="text-xs font-bold text-cyan-400 flex items-center gap-1.5">
                                <span class="w-2.5 h-2.5 bg-cyan-500 rounded-full inline-block"></span> 실시간 포물선 궤적 ($y - x$ 그래프)
                            </span>
                        </div>
                        
                        <!-- Custom Canvas for Graph plotting -->
                        <div class="w-full h-80 bg-slate-950/80 rounded-xl border border-slate-900 overflow-hidden relative">
                            <canvas id="chart-canvas" class="w-full h-full"></canvas>
                        </div>
                    </div>

                    <!-- Independent Component Graphs (x-t, y-t) in grids -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="glass rounded-2xl p-4 border border-slate-800">
                            <h4 class="text-xs text-slate-400 font-bold mb-2 flex justify-between">
                                <span>수평 등속 직선 운동 ($x - t$)</span>
                                <span class="text-cyan-400 font-mono font-bold">기울기 = v₀·cos(θ)</span>
                            </h4>
                            <div class="h-44 bg-slate-950/80 rounded-xl overflow-hidden">
                                <canvas id="xt-canvas" class="w-full h-full"></canvas>
                            </div>
                        </div>
                        <div class="glass rounded-2xl p-4 border border-slate-800">
                            <h4 class="text-xs text-slate-400 font-bold mb-2 flex justify-between">
                                <span>수직 등가속도 운동 ($y - t$)</span>
                                <span class="text-rose-400 font-mono font-bold">가속도 = -g</span>
                            </h4>
                            <div class="h-44 bg-slate-950/80 rounded-xl overflow-hidden">
                                <canvas id="yt-canvas" class="w-full h-full"></canvas>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 3: Physics Calculator -->
            <div id="tab-calculator" class="hidden glass rounded-2xl p-6 border border-slate-800 animate-fadeIn space-y-6">
                <div class="max-w-xl">
                    <h3 class="text-lg font-black text-white">물리 자동 수학 계산기</h3>
                    <p class="text-xs text-slate-400 mt-1">사용자가 직접 입력하는 환경 매개변수를 기준으로 자유롭게 포물선 주요 산출 물리량을 도출해 냅니다. 탐구 과제 보고서의 수치적 증빙으로 활용하기에 최적입니다.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div class="space-y-1">
                        <label class="text-xs text-slate-400 font-bold">초기 속도 (v₀)</label>
                        <div class="relative">
                            <input type="number" id="calc-v0" value="15" step="0.5" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm text-cyan-400 font-bold focus:outline-none focus:border-cyan-500">
                            <span class="absolute right-3 top-3 text-xs text-slate-500">m/s</span>
                        </div>
                    </div>
                    <div class="space-y-1">
                        <label class="text-xs text-slate-400 font-bold">발사 각도 (θ)</label>
                        <div class="relative">
                            <input type="number" id="calc-theta" value="45" step="1" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm text-emerald-400 font-bold focus:outline-none focus:border-emerald-500">
                            <span class="absolute right-3 top-3 text-xs text-slate-500">deg</span>
                        </div>
                    </div>
                    <div class="space-y-1">
                        <label class="text-xs text-slate-400 font-bold">초기 높이 (h)</label>
                        <div class="relative">
                            <input type="number" id="calc-h" value="3" step="0.5" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm text-pink-400 font-bold focus:outline-none focus:border-pink-500">
                            <span class="absolute right-3 top-3 text-xs text-slate-500">m</span>
                        </div>
                    </div>
                    <div class="space-y-1">
                        <label class="text-xs text-slate-400 font-bold">중력 가속도 (g)</label>
                        <div class="relative">
                            <input type="number" id="calc-g" value="9.8" step="0.1" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-sm text-yellow-400 font-bold focus:outline-none focus:border-yellow-500">
                            <span class="absolute right-3 top-3 text-xs text-slate-500">m/s²</span>
                        </div>
                    </div>
                </div>

                <div class="flex justify-end border-t border-slate-800 pt-4">
                    <button onclick="calculatePhysics()" class="py-3 px-6 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-bold text-sm shadow transition">
                        <i class="fa-solid fa-circle-check mr-1.5"></i> 정밀 시뮬레이션 계산
                    </button>
                </div>

                <!-- Calculator outputs -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
                    <div class="bg-slate-900/50 rounded-2xl p-4 border border-slate-800 space-y-1 text-center">
                        <span class="text-xs text-slate-400">총 비행 시간 (t)</span>
                        <div class="text-2xl font-black text-white font-mono" id="calc-res-t">0.00 s</div>
                        <p class="text-[10px] text-slate-500 leading-tight pt-1">지면에 착지하기까지의 시간</p>
                    </div>
                    <div class="bg-slate-900/50 rounded-2xl p-4 border border-slate-800 space-y-1 text-center">
                        <span class="text-xs text-slate-400">수평 도달 거리 (x)</span>
                        <div class="text-2xl font-black text-amber-400 font-mono" id="calc-res-x">0.00 m</div>
                        <p class="text-[10px] text-slate-500 leading-tight pt-1">등속 직선 성분의 이동 한계</p>
                    </div>
                    <div class="bg-slate-900/50 rounded-2xl p-4 border border-slate-800 space-y-1 text-center">
                        <span class="text-xs text-slate-400">최고 비행 높이 (Y_max)</span>
                        <div class="text-2xl font-black text-emerald-400 font-mono" id="calc-res-ymax">0.00 m</div>
                        <p class="text-[10px] text-slate-500 leading-tight pt-1">포물선 궤도의 가장 높은 마루점</p>
                    </div>
                    <div class="bg-slate-900/50 rounded-2xl p-4 border border-slate-800 space-y-1 text-center">
                        <span class="text-xs text-slate-400">지면 충돌 최종속도 (v_f)</span>
                        <div class="text-2xl font-black text-rose-400 font-mono" id="calc-res-vf">0.00 m/s</div>
                        <p class="text-[10px] text-slate-500 leading-tight pt-1">수평과 수직 속도벡터의 기하평균</p>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Global Setting Modal (Settings) -->
    <div id="settings-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-4 hidden">
        <div class="glass rounded-2xl p-6 max-w-sm w-full border border-slate-800 space-y-5 text-left">
            <div class="flex justify-between items-center border-b border-slate-800 pb-2">
                <h3 class="text-md font-black text-white flex items-center gap-1.5">
                    <i class="fa-solid fa-gear text-cyan-400"></i> 물리 환경 상세설정
                </h3>
                <button onclick="closeSettings()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <div class="space-y-4">
                <div class="space-y-1.5">
                    <label class="text-xs text-slate-400 font-bold block">중력 가속도 기본 프리셋</label>
                    <select id="preset-g" onchange="setGravityPreset(this.value)" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-xs text-slate-300 focus:outline-none">
                        <option value="9.8">지구 (g = 9.8 m/s²)</option>
                        <option value="1.62">달 (g = 1.62 m/s²)</option>
                        <option value="3.71">화성 (g = 3.71 m/s²)</option>
                        <option value="24.79">목성 (g = 24.79 m/s²)</option>
                    </select>
                </div>

                <div class="space-y-1.5">
                    <label class="text-xs text-slate-400 font-bold block">공기 저항 계수 (k)</label>
                    <div class="flex items-center gap-4">
                        <input type="range" id="param-drag" min="0" max="0.3" step="0.01" value="0" class="flex-grow h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-cyan-400">
                        <span id="drag-display-val" class="text-xs text-slate-300 font-bold font-mono w-10 text-right">0.00</span>
                    </div>
                </div>

                <div class="space-y-1.5">
                    <label class="text-xs text-slate-400 font-bold block">난이도 설정 (오차 한계폭 변경)</label>
                    <select id="preset-diff" class="w-full bg-slate-900 border border-slate-700 rounded-lg p-2.5 text-xs text-slate-300 focus:outline-none">
                        <option value="easy">쉬움 (오차한계 ±1.5m)</option>
                        <option value="normal" selected>보통 (오차한계 ±1.0m)</option>
                        <option value="hard">매우 어려움 (오차한계 ±0.5m)</option>
                    </select>
                </div>
            </div>

            <button onclick="saveAndApplySettings()" class="w-full py-2.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition">
                설정 저장 및 게임 리셋
            </button>
        </div>
    </div>

    <!-- Footer -->
    <footer class="glass border-t border-slate-800/80 py-4 text-center text-xs text-slate-500">
        <p>© 2026 물리학 2 창의 융합 활동 - 30806 김성준 | 분수대에 동전 넣기 시뮬레이션 앱 v1.2</p>
    </footer>

    <!-- JavaScript For App Logic, Animation, Graphics & Math -->
    <script>
        // --- Global State ---
        let currentScreen = 'home'; // 'home' | 'game' | 'learn'
        let currentTab = 'theory'; // 'theory' | 'graph' | 'calculator'
        
        // Physics Environment Constants
        let g_accel = 9.8; // Gravity (m/s2)
        let air_drag_k = 0.00; // Drag constant
        let game_difficulty = 'normal'; // 'easy' | 'normal' | 'hard'
        
        // Game variables
        let level = 1;
        let lives = 3;
        let score = 0;
        let bestScore = 0;
        let isPaused = false;
        
        // Target fountain specs
        let targetX = 15.0; // Target distance (meters)
        let targetWidth = 2.0; // Target width (meters)
        let targetTolerance = 1.0; // Acceptable error
        let windFactor = 0.0; // Level wind (horizontal force/accel)

        // Coin Simulation state
        let coin = {
            active: false,
            x: 0, // dynamic positions in meters
            y: 0,
            vx: 0, // dynamic velocities
            vy: 0,
            t: 0, // elapsed time
            spinAngle: 0,
            trail: [] // historical coordinate array
        };

        // Splash Particles Struct (for coin impact)
        let particles = [];
        
        // Shimmering Fountain Water Drops (persistent animated fountain water)
        let fountainDrops = [];

        // Canvas setups
        let mainCanvas, mainCtx;
        let graphCanvas, graphCtx;
        let xtCanvas, xtCtx;
        let ytCanvas, ytCtx;

        // Scaling factors
        let originPx = { x: 80, y: 310 }; 
        const pxPerMeter = 18; // scale factor

        // --- Screen & State Routers ---
        window.onload = function() {
            // Load saved high scores
            const savedBest = localStorage.getItem('coin_toss_best');
            if(savedBest) {
                bestScore = parseInt(savedBest);
                document.getElementById('best-score-display').innerText = bestScore + ' 점';
            }

            // Init Main Simulation Canvas
            mainCanvas = document.getElementById('physics-canvas');
            mainCtx = mainCanvas.getContext('2d');
            
            // Initial container measurement
            resizeMainCanvas();
            
            window.addEventListener('resize', () => {
                resizeMainCanvas();
                if(currentScreen === 'learn' && currentTab === 'graph') {
                    resizeGraphCanvases();
                    drawInteractiveGraphs();
                }
                drawScene();
            });

            // Sliders listener setup
            setupControls();

            // Set Initial Predictions
            updatePredictions();

            // Initialize Background loop
            requestAnimationFrame(simLoop);
        };

        function resizeMainCanvas() {
            const rect = mainCanvas.parentNode.getBoundingClientRect();
            mainCanvas.width = rect.width || 600;
            mainCanvas.height = rect.height || 384;
            originPx.y = mainCanvas.height - 74;
        }

        function resizeGraphCanvases() {
            if (graphCanvas) {
                const rect = graphCanvas.parentNode.getBoundingClientRect();
                graphCanvas.width = rect.width || 400;
                graphCanvas.height = rect.height || 320;
            }
            if (xtCanvas) {
                const rect = xtCanvas.parentNode.getBoundingClientRect();
                xtCanvas.width = rect.width || 200;
                xtCanvas.height = rect.height || 176;
            }
            if (ytCanvas) {
                const rect = ytCanvas.parentNode.getBoundingClientRect();
                ytCanvas.width = rect.width || 200;
                ytCanvas.height = rect.height || 176;
            }
        }

        function goHome() {
            hideAllScreens();
            document.getElementById('home-screen').classList.remove('hidden');
            currentScreen = 'home';
        }

        function startGame() {
            hideAllScreens();
            document.getElementById('game-screen').classList.remove('hidden');
            currentScreen = 'game';
            resizeMainCanvas(); 
            initLevel();
            drawScene();
        }

        function goLearn() {
            hideAllScreens();
            document.getElementById('learn-screen').classList.remove('hidden');
            currentScreen = 'learn';
            switchTab(currentTab);
        }

        function hideAllScreens() {
            document.getElementById('home-screen').classList.add('hidden');
            document.getElementById('game-screen').classList.add('hidden');
            document.getElementById('learn-screen').classList.add('hidden');
            document.getElementById('settings-modal').classList.add('hidden');
            document.getElementById('result-modal').classList.add('hidden');
        }

        // --- Tab Management ---
        function switchTab(tabId) {
            currentTab = tabId;
            document.getElementById('tab-theory').classList.add('hidden');
            document.getElementById('tab-graph').classList.add('hidden');
            document.getElementById('tab-calculator').classList.add('hidden');
            
            document.getElementById('tab-theory-btn').className = "flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-slate-400 hover:text-slate-200";
            document.getElementById('tab-graph-btn').className = "flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-slate-400 hover:text-slate-200";
            document.getElementById('tab-calculator-btn').className = "flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-slate-400 hover:text-slate-200";

            if(tabId === 'theory') {
                document.getElementById('tab-theory').classList.remove('hidden');
                document.getElementById('tab-theory-btn').className = "flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-cyan-400 bg-slate-800 shadow";
            } else if(tabId === 'graph') {
                document.getElementById('tab-graph').classList.remove('hidden');
                document.getElementById('tab-graph-btn').className = "flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-cyan-400 bg-slate-800 shadow";
                
                graphCanvas = document.getElementById('chart-canvas');
                xtCanvas = document.getElementById('xt-canvas');
                ytCanvas = document.getElementById('yt-canvas');
                
                resizeGraphCanvases();
                initGraphCanvases();
                drawInteractiveGraphs();
            } else if(tabId === 'calculator') {
                document.getElementById('tab-calculator').classList.remove('hidden');
                document.getElementById('tab-calculator-btn').className = "flex-1 md:flex-none px-4 py-2 rounded-lg text-xs font-bold transition text-cyan-400 bg-slate-800 shadow";
                calculatePhysics();
            }
        }

        // --- Settings Management ---
        function openSettings() {
            document.getElementById('settings-modal').classList.remove('hidden');
        }

        function closeSettings() {
            document.getElementById('settings-modal').classList.add('hidden');
        }

        function setGravityPreset(val) {
            document.getElementById('env-g').innerText = val;
        }

        function saveAndApplySettings() {
            g_accel = parseFloat(document.getElementById('preset-g').value);
            air_drag_k = parseFloat(document.getElementById('param-drag').value);
            game_difficulty = document.getElementById('preset-diff').value;

            document.getElementById('env-g').innerText = g_accel;
            document.getElementById('env-k').innerText = air_drag_k.toFixed(2);
            document.getElementById('drag-display-val').innerText = air_drag_k.toFixed(2);

            if(game_difficulty === 'easy') {
                targetTolerance = 1.5;
            } else if(game_difficulty === 'normal') {
                targetTolerance = 1.0;
            } else {
                targetTolerance = 0.5;
            }

            closeSettings();
            initLevel();
        }

        document.getElementById('param-drag').addEventListener('input', function(e) {
            document.getElementById('drag-display-val').innerText = parseFloat(e.target.value).toFixed(2);
        });

        // --- Controls Synchronizer ---
        function setupControls() {
            const v0_sl = document.getElementById('v0-slider');
            const v0_num = document.getElementById('v0-num');
            const th_sl = document.getElementById('theta-slider');
            const th_num = document.getElementById('theta-num');
            const h_sl = document.getElementById('h-slider');

            const bindInputs = (slider, num, callback) => {
                slider.addEventListener('input', (e) => {
                    num.value = e.target.value;
                    callback();
                });
                num.addEventListener('change', (e) => {
                    slider.value = e.target.value;
                    callback();
                });
            };

            bindInputs(v0_sl, v0_num, () => { updatePredictions(); drawScene(); });
            bindInputs(th_sl, th_num, () => { updatePredictions(); drawScene(); });
            
            h_sl.addEventListener('input', (e) => {
                document.getElementById('h-val').innerText = parseFloat(e.target.value).toFixed(1) + 'm';
                updatePredictions();
                drawScene();
            });
        }

        // --- Level Creator ---
        function initLevel() {
            targetX = 10.0 + (level * 3.2); 
            targetWidth = Math.max(1.2, 3.0 - (level * 0.3)); 
            
            if(level >= 3) {
                windFactor = (Math.random() * 4 - 2); 
                document.getElementById('wind-indicator').classList.remove('hidden');
                document.getElementById('wind-value').innerText = `${windFactor > 0 ? '▶ ' : '◀ '}${Math.abs(windFactor).toFixed(1)} m/s²`;
            } else {
                windFactor = 0.0;
                document.getElementById('wind-indicator').classList.add('hidden');
            }

            document.getElementById('game-level').innerText = level;
            document.getElementById('game-score').innerText = score;
            document.getElementById('target-dist').innerText = targetX.toFixed(1);
            document.getElementById('target-width').innerText = targetWidth.toFixed(1);
            document.getElementById('target-tolerance').innerText = targetTolerance.toFixed(1);

            const lc = document.getElementById('lives-container');
            lc.innerHTML = '';
            for(let i=0; i<3; i++) {
                const coinHeart = document.createElement('i');
                coinHeart.className = i < lives ? "fa-solid fa-coins text-yellow-400 text-sm" : "fa-solid fa-circle text-slate-700 text-[10px]";
                lc.appendChild(coinHeart);
            }

            coin.active = false;
            updatePredictions();
            drawScene();
        }

        // --- Prediction Math ---
        function getLauncherParams() {
            return {
                v0: parseFloat(document.getElementById('v0-slider').value),
                theta: parseFloat(document.getElementById('theta-slider').value) * Math.PI / 180,
                h: parseFloat(document.getElementById('h-slider').value)
            };
        }

        function updatePredictions() {
            const { v0, theta, h } = getLauncherParams();
            const g = g_accel;

            const vx0 = v0 * Math.cos(theta);
            const vy0 = v0 * Math.sin(theta);

            const a = 0.5 * g;
            const b = -vy0;
            const c = -h;
            
            let t_flight = 0;
            if(a > 0) {
                const disc = b*b - 4*a*c;
                if(disc >= 0) {
                    t_flight = (-b + Math.sqrt(disc)) / (2*a);
                }
            }

            const x_range = vx0 * t_flight;
            
            let peak_y = h;
            if (vy0 > 0) {
                const t_peak = vy0 / g;
                peak_y = h + (vy0 * t_peak) - (0.5 * g * t_peak * t_peak);
            }

            document.getElementById('pred-t').innerText = t_flight.toFixed(2) + ' s';
            document.getElementById('pred-x').innerText = x_range.toFixed(2) + ' m';
            document.getElementById('pred-y').innerText = peak_y.toFixed(2) + ' m';
        }

        // --- Coin Thrower Launcher ---
        function launchCoin() {
            if(coin.active) return; 

            const { v0, theta, h } = getLauncherParams();
            
            coin.x = 0;
            coin.y = h;
            coin.vx = v0 * Math.cos(theta);
            coin.vy = v0 * Math.sin(theta);
            coin.t = 0;
            coin.spinAngle = 0;
            coin.trail = [];
            coin.active = true;

            document.getElementById('btn-fire').disabled = true;
            document.getElementById('btn-fire').classList.add('opacity-50');
        }

        // --- Main Simulation Loop ---
        function simLoop(timestamp) {
            if(currentScreen === 'game' && !isPaused) {
                updatePhysics();
                drawScene();
            }
            requestAnimationFrame(simLoop);
        }

        function updatePhysics() {
            for(let i=particles.length-1; i>=0; i--) {
                const p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.vy += 0.25;
                p.alpha -= 0.02;
                if(p.alpha <= 0) particles.splice(i, 1);
            }

            const targetCenterPx = originPx.x + (targetX * pxPerMeter);
            if (Math.random() < 0.4) { 
                fountainDrops.push({
                    x: targetCenterPx + (Math.random() * 4 - 2),
                    y: originPx.y - 58,
                    vx: (Math.random() * 1.4 - 0.7),
                    vy: -(Math.random() * 2.5 + 3.5),
                    alpha: 1.0,
                    size: Math.random() * 1.8 + 1
                });
            }

            for(let i=fountainDrops.length-1; i>=0; i--) {
                const d = fountainDrops[i];
                d.x += d.vx;
                d.y += d.vy;
                d.vy += 0.16; 
                d.alpha -= 0.015;
                if (d.y > originPx.y - 12 || d.alpha <= 0) {
                    fountainDrops.splice(i, 1);
                }
            }

            if(!coin.active) return;

            const dt = 0.016; 
            coin.t += dt;
            coin.spinAngle += 0.18; 

            coin.trail.push({ x: coin.x, y: coin.y });
            if(coin.trail.length > 50) coin.trail.shift();

            const ax = -air_drag_k * coin.vx + windFactor;
            const ay = -g_accel - air_drag_k * coin.vy;

            coin.vx += ax * dt;
            coin.vy += ay * dt;

            coin.x += coin.vx * dt;
            coin.y += coin.vy * dt;

            if(coin.y <= 0) {
                coin.y = 0;
                coin.active = false;
                spawnWaterSplash(coin.x);
                setTimeout(evaluateResult, 650);
            }
        }

        function spawnWaterSplash(impactX) {
            const isSuccess = Math.abs(impactX - targetX) <= (targetWidth / 2);
            const color = isSuccess ? '#22d3ee' : '#cbd5e1';
            
            for(let i=0; i<30; i++) {
                particles.push({
                    x: originPx.x + (impactX * pxPerMeter),
                    y: originPx.y,
                    vx: (Math.random() * 5 - 2.5),
                    vy: -(Math.random() * 7 + 4),
                    alpha: 1.0,
                    color: color
                });
            }
        }

        // --- Evaluator & Analytics ---
        function evaluateResult() {
            document.getElementById('btn-fire').disabled = false;
            document.getElementById('btn-fire').classList.remove('opacity-50');

            const diffX = Math.abs(coin.x - targetX);
            const isSuccess = diffX <= (targetWidth / 2);

            addToHistory(isSuccess);

            document.getElementById('res-v0').innerText = parseFloat(document.getElementById('v0-slider').value).toFixed(1);
            document.getElementById('res-theta').innerText = document.getElementById('theta-slider').value;
            document.getElementById('res-t').innerText = coin.t.toFixed(2);
            document.getElementById('res-x').innerText = coin.x.toFixed(2);
            
            const errorVal = coin.x - targetX;
            document.getElementById('res-error').innerText = `${errorVal >= 0 ? '+' : ''}${errorVal.toFixed(2)} m`;
            document.getElementById('res-error').className = isSuccess ? 'text-emerald-400 font-bold' : 'text-rose-400 font-bold';

            const badge = document.getElementById('result-badge');
            const title = document.getElementById('result-title');
            const msg = document.getElementById('result-msg');
            const glow = document.getElementById('result-radial-glow');
            const tip = document.getElementById('result-physics-tip');
            const btnPrimary = document.getElementById('btn-result-primary');

            if(isSuccess) {
                badge.innerText = "SUCCESS";
                badge.className = "px-3 py-1 rounded-full text-xs font-black bg-emerald-950 text-emerald-400 border border-emerald-800";
                title.innerText = "동전이 들어갔습니다! 🎉";
                msg.innerText = "정밀한 물리적 조작으로 분수대 표적 골인에 성공했습니다.";
                glow.style.backgroundColor = "rgba(16, 185, 129, 0.4)";
                
                score += 100 * level;
                if(score > bestScore) {
                    bestScore = score;
                    localStorage.setItem('coin_toss_best', bestScore);
                    document.getElementById('best-score-display').innerText = bestScore + ' 점';
                }

                tip.innerText = "훌륭합니다! 분속 궤도는 등속 수평 성분과 등가속 수직 성분이 완벽히 매칭되어 목표 사거리에 도달했습니다. 다음 단계에서는 타겟 거리가 바뀌며 바람의 영향이 거세질 수 있습니다.";
                btnPrimary.innerText = "다음 레벨 도전";
            } else {
                badge.innerText = "FAILED";
                badge.className = "px-3 py-1 rounded-full text-xs font-black bg-rose-950 text-rose-400 border border-rose-800";
                title.innerText = "아쉽네요! 궤도를 벗어났습니다.";
                msg.innerText = "조금만 더 정밀하게 힘을 조정해 볼까요?";
                glow.style.backgroundColor = "rgba(244, 63, 94, 0.4)";

                lives--;

                if(coin.x < targetX) {
                    tip.innerText = `현재 수평 도달거리(${coin.x.toFixed(1)}m)가 목표 거리(${targetX.toFixed(1)}m)보다 부족합니다. 수평 초기속도 v₀를 늘리거나, 발사 높이를 더 확보하거나, 각도를 45° 쪽으로 수정하여 비행시간을 확장하세요.`;
                } else {
                    tip.innerText = `동전이 분수대를 훌쩍 뛰어넘어 과도하게 도달(${coin.x.toFixed(1)}m)하였습니다. 초기 속도를 약간 감속하거나 각도를 급격하게 좁히거나 높여서 비행 궤적을 낮추어 보세요.`;
                }

                btnPrimary.innerText = "다시 시도";
                if(lives <= 0) {
                    btnPrimary.innerText = "레벨 초기화 및 재시작";
                }
            }

            document.getElementById('result-modal').classList.remove('hidden');
        }

        function closeResultModal(advance) {
            document.getElementById('result-modal').classList.add('hidden');
            if(advance) {
                if(lives <= 0) {
                    level = 1;
                    lives = 3;
                    score = 0;
                    initLevel();
                } else {
                    level++;
                    initLevel();
                }
            } else {
                if(lives <= 0) {
                    level = 1;
                    lives = 3;
                    score = 0;
                    initLevel();
                } else {
                    initLevel();
                }
            }
        }

        // --- History logging ---
        function addToHistory(isSuccess) {
            const historyLog = document.getElementById('history-log');
            
            if (historyLog.innerHTML.includes('아직 시도한 실험이 없습니다.')) {
                historyLog.innerHTML = '';
            }

            const { v0, theta, h } = getLauncherParams();
            const logItem = document.createElement('div');
            logItem.className = `flex justify-between items-center p-2 rounded border ${isSuccess ? 'bg-emerald-950/20 border-emerald-900/30 text-emerald-300' : 'bg-slate-900 border-slate-800 text-slate-300'}`;
            
            logItem.innerHTML = `
                <div>
                    <span class="font-bold ${isSuccess ? 'text-emerald-400' : 'text-slate-400'}">[#시도]</span>
                    v₀:${v0}m/s | θ:${theta}° | t:${coin.t.toFixed(2)}s
                </div>
                <div class="flex items-center gap-2">
                    <span>x_낙하: <b>${coin.x.toFixed(2)}m</b></span>
                    <span class="text-[9px] px-1 rounded ${isSuccess ? 'bg-emerald-500 text-emerald-950 font-bold' : 'bg-rose-500/20 text-rose-400'}">
                        ${isSuccess ? '골인' : '실패'}
                    </span>
                </div>
            `;
            historyLog.prepend(logItem);
        }

        function clearHistory() {
            document.getElementById('history-log').innerHTML = '<div class="text-slate-500 italic text-center py-8">아직 시도한 실험이 없습니다.</div>';
        }

        // --- Scene Visual Renderer ---
        function drawScene() {
            if(!mainCtx || mainCanvas.width === 0 || mainCanvas.height === 0) return;
            mainCtx.clearRect(0, 0, mainCanvas.width, mainCanvas.height);

            const { v0, theta, h } = getLauncherParams();

            // Ground Line
            mainCtx.beginPath();
            mainCtx.moveTo(0, originPx.y);
            mainCtx.lineTo(mainCanvas.width, originPx.y);
            mainCtx.strokeStyle = '#334155';
            mainCtx.lineWidth = 4;
            mainCtx.stroke();

            // Ground tiling
            mainCtx.fillStyle = '#0f172a';
            mainCtx.fillRect(0, originPx.y + 2, mainCanvas.width, mainCanvas.height - originPx.y);

            // 1. Draw Target Classical Stone Fountain
            const targetCenterPx = originPx.x + (targetX * pxPerMeter);
            const targetWidthPx = targetWidth * pxPerMeter;

            const grayMarbleGrad = mainCtx.createLinearGradient(targetCenterPx - targetWidthPx, 0, targetCenterPx + targetWidthPx, 0);
            grayMarbleGrad.addColorStop(0, '#1e293b');
            grayMarbleGrad.addColorStop(0.3, '#475569');
            grayMarbleGrad.addColorStop(0.5, '#cbd5e1'); 
            grayMarbleGrad.addColorStop(0.7, '#475569');
            grayMarbleGrad.addColorStop(1, '#0f172a');

            const lightMarbleGrad = mainCtx.createLinearGradient(targetCenterPx - 15, 0, targetCenterPx + 15, 0);
            lightMarbleGrad.addColorStop(0, '#334155');
            lightMarbleGrad.addColorStop(0.5, '#94a3b8');
            lightMarbleGrad.addColorStop(1, '#1e293b');

            // --- 1단: 바닥 대형 Basin ---
            mainCtx.fillStyle = grayMarbleGrad;
            mainCtx.strokeStyle = '#475569';
            mainCtx.lineWidth = 2;
            mainCtx.beginPath();
            mainCtx.roundRect(targetCenterPx - targetWidthPx * 0.7, originPx.y - 12, targetWidthPx * 1.4, 12, [4, 4, 0, 0]);
            mainCtx.fill();
            mainCtx.stroke();

            mainCtx.fillStyle = 'rgba(6, 182, 212, 0.4)';
            mainCtx.beginPath();
            mainCtx.ellipse(targetCenterPx, originPx.y - 12, targetWidthPx * 0.65, 4, 0, 0, 2 * Math.PI);
            mainCtx.fill();

            // --- 2단: 중간 기둥 및 중간 Bowl ---
            mainCtx.fillStyle = lightMarbleGrad;
            mainCtx.beginPath();
            mainCtx.moveTo(targetCenterPx - 12, originPx.y - 12);
            mainCtx.quadraticCurveTo(targetCenterPx - 8, originPx.y - 25, targetCenterPx - 14, originPx.y - 35);
            mainCtx.lineTo(targetCenterPx + 14, originPx.y - 35);
            mainCtx.quadraticCurveTo(targetCenterPx + 8, originPx.y - 25, targetCenterPx + 12, originPx.y - 12);
            mainCtx.closePath();
            mainCtx.fill();
            mainCtx.stroke();

            mainCtx.fillStyle = grayMarbleGrad;
            mainCtx.beginPath();
            mainCtx.ellipse(targetCenterPx, originPx.y - 35, targetWidthPx * 0.45, 7, 0, 0, 2 * Math.PI);
            mainCtx.fill();
            mainCtx.stroke();

            mainCtx.fillStyle = 'rgba(34, 211, 238, 0.45)';
            mainCtx.beginPath();
            mainCtx.ellipse(targetCenterPx, originPx.y - 36, targetWidthPx * 0.42, 5, 0, 0, 2 * Math.PI);
            mainCtx.fill();

            // --- 3단: 상부 가는 기둥 및 상부 소형 Bowl ---
            mainCtx.fillStyle = lightMarbleGrad;
            mainCtx.beginPath();
            mainCtx.moveTo(targetCenterPx - 7, originPx.y - 35);
            mainCtx.quadraticCurveTo(targetCenterPx - 4, originPx.y - 48, targetCenterPx - 8, originPx.y - 58);
            mainCtx.lineTo(targetCenterPx + 8, originPx.y - 58);
            mainCtx.quadraticCurveTo(targetCenterPx + 4, originPx.y - 48, targetCenterPx + 7, originPx.y - 35);
            mainCtx.closePath();
            mainCtx.fill();
            mainCtx.stroke();

            mainCtx.fillStyle = grayMarbleGrad;
            mainCtx.beginPath();
            mainCtx.ellipse(targetCenterPx, originPx.y - 58, targetWidthPx * 0.25, 4, 0, 0, 2 * Math.PI);
            mainCtx.fill();
            mainCtx.stroke();

            mainCtx.fillStyle = 'rgba(103, 232, 249, 0.6)';
            mainCtx.beginPath();
            mainCtx.ellipse(targetCenterPx, originPx.y - 59, targetWidthPx * 0.22, 2.5, 0, 0, 2 * Math.PI);
            mainCtx.fill();

            const seconds = Date.now() / 1000;
            mainCtx.lineWidth = 1.5;
            
            mainCtx.strokeStyle = 'rgba(34, 211, 238, 0.65)';
            mainCtx.beginPath();
            mainCtx.arc(targetCenterPx - 10, originPx.y - 52, 10 + Math.sin(seconds * 4) * 1.5, Math.PI * 0.9, 0);
            mainCtx.stroke();
            
            mainCtx.beginPath();
            mainCtx.arc(targetCenterPx + 10, originPx.y - 52, 10 + Math.cos(seconds * 4) * 1.5, Math.PI, 0.1 * Math.PI);
            mainCtx.stroke();

            mainCtx.strokeStyle = 'rgba(6, 182, 212, 0.45)';
            mainCtx.beginPath();
            mainCtx.arc(targetCenterPx - 22, originPx.y - 25, 14 + Math.sin(seconds * 3.5) * 2, Math.PI * 0.95, 0.05 * Math.PI);
            mainCtx.stroke();

            mainCtx.beginPath();
            mainCtx.arc(targetCenterPx + 22, originPx.y - 25, 14 + Math.cos(seconds * 3.5) * 2, Math.PI * 0.95, 0.05 * Math.PI);
            mainCtx.stroke();

            mainCtx.strokeStyle = 'rgba(165, 243, 252, 0.85)';
            mainCtx.lineWidth = 2.2;
            mainCtx.beginPath();
            mainCtx.moveTo(targetCenterPx, originPx.y - 58);
            mainCtx.quadraticCurveTo(targetCenterPx, originPx.y - 82 - Math.sin(seconds * 5) * 3, targetCenterPx + 0.5, originPx.y - 58);
            mainCtx.stroke();

            for (let d of fountainDrops) {
                mainCtx.fillStyle = `rgba(165, 243, 252, ${d.alpha})`;
                mainCtx.beginPath();
                mainCtx.arc(d.x, d.y, d.size, 0, Math.PI * 2);
                mainCtx.fill();
            }

            // 2. Elevated Platform Base
            const launchH_px = h * pxPerMeter;
            mainCtx.fillStyle = '#1e293b';
            mainCtx.fillRect(originPx.x - 20, originPx.y - launchH_px, 25, launchH_px);
            mainCtx.strokeStyle = '#334155';
            mainCtx.lineWidth = 1.5;
            mainCtx.strokeRect(originPx.x - 20, originPx.y - launchH_px, 25, launchH_px);

            // Launcher Nozzle Cylinder
            mainCtx.save();
            mainCtx.translate(originPx.x - 7, originPx.y - launchH_px);
            mainCtx.rotate(-theta);
            
            mainCtx.fillStyle = '#475569';
            mainCtx.fillRect(0, -6, 22, 12);
            mainCtx.strokeStyle = '#94a3b8';
            mainCtx.lineWidth = 1.5;
            mainCtx.strokeRect(0, -6, 22, 12);
            mainCtx.restore();

            mainCtx.fillStyle = '#475569';
            mainCtx.font = '8px monospace';
            mainCtx.fillText('x=0m', originPx.x - 12, originPx.y + 14);

            // 3. Draw Preview Path
            if(!coin.active) {
                drawPreviewTrajectory(v0, theta, h);
            }

            // Splash particles
            for(let p of particles) {
                mainCtx.fillStyle = p.color;
                mainCtx.globalAlpha = p.alpha;
                mainCtx.beginPath();
                mainCtx.arc(p.x, p.y, 2.5, 0, Math.PI*2);
                mainCtx.fill();
            }
            mainCtx.globalAlpha = 1.0; 

            // 4. Draw Active Spinning Coin & Trail
            if(coin.active) {
                if(coin.trail.length > 1) {
                    mainCtx.beginPath();
                    mainCtx.strokeStyle = 'rgba(245, 158, 11, 0.4)';
                    mainCtx.lineWidth = 3.5;
                    const startPx = physicsToCanvas(coin.trail[0].x, coin.trail[0].y);
                    mainCtx.moveTo(startPx.x, startPx.y);
                    for(let i=1; i<coin.trail.length; i++) {
                        const pt = physicsToCanvas(coin.trail[i].x, coin.trail[i].y);
                        mainCtx.lineTo(pt.x, pt.y);
                    }
                    mainCtx.stroke();
                }

                const coinPx = physicsToCanvas(coin.x, coin.y);
                mainCtx.save();
                mainCtx.translate(coinPx.x, coinPx.y);
                mainCtx.scale(Math.abs(Math.sin(coin.spinAngle)), 1.0); 

                mainCtx.beginPath();
                mainCtx.arc(0, 0, 9, 0, Math.PI * 2);
                mainCtx.fillStyle = '#d97706';
                mainCtx.fill();

                mainCtx.beginPath();
                mainCtx.arc(0, 0, 7.5, 0, Math.PI * 2);
                mainCtx.fillStyle = '#fbbf24';
                mainCtx.fill();

                mainCtx.fillStyle = '#78350f';
                mainCtx.font = 'black 9px Arial';
                mainCtx.textAlign = 'center';
                mainCtx.textBaseline = 'middle';
                mainCtx.fillText('₩', 0, 0);

                mainCtx.restore();
            }
        }

        function drawPreviewTrajectory(v0, theta_rad, h) {
            mainCtx.beginPath();
            mainCtx.setLineDash([3, 4]);
            mainCtx.strokeStyle = 'rgba(148, 163, 184, 0.4)';
            mainCtx.lineWidth = 1.2;

            const t_max = 5;
            let first = true;

            let px_x = 0;
            let px_y = h;
            let vx = v0 * Math.cos(theta_rad);
            let vy = v0 * Math.sin(theta_rad);
            const dt = 0.05;

            for(let t=0; t<t_max; t+=dt) {
                const cvPt = physicsToCanvas(px_x, px_y);
                
                if(first) {
                    mainCtx.moveTo(cvPt.x, cvPt.y);
                    first = false;
                } else {
                    mainCtx.lineTo(cvPt.x, cvPt.y);
                }

                const ax = -air_drag_k * vx + windFactor;
                const ay = -g_accel - air_drag_k * vy;
                
                vx += ax * dt;
                vy += ay * dt;
                px_x += vx * dt;
                px_y += vy * dt;

                if(px_y < 0) break;
            }
            mainCtx.stroke();
            mainCtx.setLineDash([]); 
        }

        function physicsToCanvas(mX, mY) {
            return {
                x: originPx.x + (mX * pxPerMeter),
                y: originPx.y - (mY * pxPerMeter)
            };
        }

        // --- Tab 2: Interactive Graph Rendering ---
        function initGraphCanvases() {
            if(!graphCanvas) return;
            graphCtx = graphCanvas.getContext('2d');
            xtCtx = xtCanvas.getContext('2d');
            ytCtx = ytCanvas.getContext('2d');

            const bindGraphEvent = (id, valId, suffix) => {
                document.getElementById(id).addEventListener('input', (e) => {
                    document.getElementById(valId).innerText = `${e.target.value} ${suffix}`;
                    drawInteractiveGraphs();
                });
            };

            bindGraphEvent('graph-v0', 'graph-v0-val', 'm/s');
            bindGraphEvent('graph-theta', 'graph-theta-val', '°');
            bindGraphEvent('graph-h', 'graph-h-val', 'm');
            bindGraphEvent('graph-g', 'graph-g-val', 'm/s²');
        }

        function drawInteractiveGraphs() {
            if(!graphCtx) return;

            const v0 = parseFloat(document.getElementById('graph-v0').value);
            const theta = parseFloat(document.getElementById('graph-theta').value) * Math.PI / 180;
            const h = parseFloat(document.getElementById('graph-h').value);
            const g = parseFloat(document.getElementById('graph-g').value);

            drawTrajectoryGraph(graphCanvas, graphCtx, v0, theta, h, g);
            drawXTGraph(xtCanvas, xtCtx, v0, theta, h, g);
            drawYTGraph(ytCanvas, ytCtx, v0, theta, h, g);
        }

        function drawTrajectoryGraph(canvas, ctx, v0, theta, h, g) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            const pad = { top: 30, right: 30, bottom: 40, left: 50 };
            const chartW = canvas.width - pad.left - pad.right;
            const chartH = canvas.height - pad.top - pad.bottom;

            const xMaxRange = 30;
            const yMaxRange = 15;

            const mapX = (x) => pad.left + (x / xMaxRange) * chartW;
            const mapY = (y) => pad.top + chartH - (y / yMaxRange) * chartH;

            ctx.strokeStyle = '#1e293b';
            ctx.lineWidth = 0.8;
            ctx.fillStyle = '#64748b';
            ctx.font = '10px monospace';
            
            for(let x=0; x<=xMaxRange; x+=5) {
                const pxX = mapX(x);
                ctx.beginPath();
                ctx.moveTo(pxX, pad.top);
                ctx.lineTo(pxX, pad.top + chartH);
                ctx.stroke();
                ctx.fillText(x + 'm', pxX - 10, pad.top + chartH + 18);
            }

            for(let y=0; y<=yMaxRange; y+=3) {
                const pxY = mapY(y);
                ctx.beginPath();
                ctx.moveTo(pad.left, pxY);
                ctx.lineTo(pad.left + chartW, pxY);
                ctx.stroke();
                ctx.fillText(y + 'm', pad.left - 30, pxY + 4);
            }

            ctx.strokeStyle = '#475569';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(pad.left, pad.top);
            ctx.lineTo(pad.left, pad.top + chartH);
            ctx.lineTo(pad.left + chartW, pad.top + chartH);
            ctx.stroke();

            ctx.strokeStyle = '#06b6d4'; 
            ctx.lineWidth = 3;
            ctx.beginPath();

            let vx0 = v0 * Math.cos(theta);
            let vy0 = v0 * Math.sin(theta);
            let first = true;

            for(let step=0; step<=200; step++) {
                const xVal = (step / 200) * xMaxRange;
                
                let yVal = 0;
                if(vx0 > 0) {
                    const t = xVal / vx0;
                    yVal = h + (vy0 * t) - (0.5 * g * t * t);
                } else {
                    yVal = h - (0.5 * g * (xVal*xVal));
                }

                if(yVal < 0) {
                    const pxX = mapX(xVal);
                    const pxY = mapY(0);
                    ctx.lineTo(pxX, pxY);
                    break;
                }

                const pxX = mapX(xVal);
                const pxY = mapY(yVal);
                
                if(first) {
                    ctx.moveTo(pxX, pxY);
                    first = false;
                } else {
                    ctx.lineTo(pxX, pxY);
                }
            }
            ctx.stroke();

            ctx.fillStyle = '#94a3b8';
            ctx.font = '10px sans-serif';
            ctx.fillText('수평거리 (x)', pad.left + chartW/2 - 20, pad.top + chartH + 32);
        }

        // x-t Graph
        function drawXTGraph(canvas, ctx, v0, theta, h, g) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const pad = { top: 20, right: 15, bottom: 25, left: 35 };
            const w = canvas.width - pad.left - pad.right;
            const hC = canvas.height - pad.top - pad.bottom;

            const tMax = 3.0;
            const xMax = 30.0;

            const mapX = (t) => pad.left + (t / tMax) * w;
            const mapY = (x) => pad.top + hC - (x / xMax) * hC;

            ctx.strokeStyle = '#334155';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(pad.left, pad.top);
            ctx.lineTo(pad.left, pad.top + hC);
            ctx.lineTo(pad.left + w, pad.top + hC);
            ctx.stroke();

            ctx.strokeStyle = '#34d399'; 
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            
            const vx0 = v0 * Math.cos(theta);
            
            ctx.moveTo(mapX(0), mapY(0));
            ctx.lineTo(mapX(tMax), mapY(vx0 * tMax));
            ctx.stroke();

            ctx.fillStyle = '#64748b';
            ctx.font = '8px monospace';
            ctx.fillText('시간(t)', pad.left + w - 25, pad.top + hC + 15);
            ctx.fillText('거리(x)', 5, pad.top + 10);
        }

        // y-t Graph
        function drawYTGraph(canvas, ctx, v0, theta, h, g) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            const pad = { top: 20, right: 15, bottom: 25, left: 35 };
            const w = canvas.width - pad.left - pad.right;
            const hC = canvas.height - pad.top - pad.bottom;

            const tMax = 3.0; 
            const yMax = 15.0; 

            const mapX = (t) => pad.left + (t / tMax) * w;
            const mapY = (y) => pad.top + hC - (y / yMax) * hC;

            ctx.strokeStyle = '#334155';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.moveTo(pad.left, pad.top);
            ctx.lineTo(pad.left, pad.top + hC);
            ctx.lineTo(pad.left + w, pad.top + hC);
            ctx.stroke();

            ctx.strokeStyle = '#f43f5e'; 
            ctx.lineWidth = 2.5;
            ctx.beginPath();

            const vy0 = v0 * Math.sin(theta);
            let first = true;

            for(let t=0; t<=tMax; t+=0.05) {
                const yVal = h + (vy0 * t) - (0.5 * g * t * t);
                if(yVal < 0) {
                    ctx.lineTo(mapX(t), mapY(0));
                    break;
                }
                const pxX = mapX(t);
                const pxY = mapY(yVal);
                
                if(first) {
                    ctx.moveTo(pxX, pxY);
                    first = false;
                } else {
                    ctx.lineTo(pxX, pxY);
                }
            }
            ctx.stroke();

            ctx.fillStyle = '#64748b';
            ctx.font = '8px monospace';
            ctx.fillText('시간(t)', pad.left + w - 25, pad.top + hC + 15);
            ctx.fillText('높이(y)', 5, pad.top + 10);
        }

        function calculatePhysics() {
            const v0 = parseFloat(document.getElementById('calc-v0').value);
            const theta_deg = parseFloat(document.getElementById('calc-theta').value);
            const theta = theta_deg * Math.PI / 180;
            const h = parseFloat(document.getElementById('calc-h').value);
            const g = parseFloat(document.getElementById('calc-g').value);

            const vx0 = v0 * Math.cos(theta);
            const vy0 = v0 * Math.sin(theta);

            const a = 0.5 * g;
            const b = -vy0;
            const c = -h;
            
            let t_flight = 0;
            if(a > 0) {
                const disc = b*b - 4*a*c;
                if(disc >= 0) {
                    t_flight = (-b + Math.sqrt(disc)) / (2*a);
                }
            }

            const x_range = vx0 * t_flight;

            let peak_y = h;
            if (vy0 > 0) {
                const t_peak = vy0 / g;
                peak_y = h + (vy0 * t_peak) - (0.5 * g * t_peak * t_peak);
            }

            const vx_f = vx0;
            const vy_f = vy0 - g * t_flight;
            const v_f = Math.sqrt(vx_f * vx_f + vy_f * vy_f);

            document.getElementById('calc-res-t').innerText = t_flight.toFixed(3) + ' s';
            document.getElementById('calc-res-x').innerText = x_range.toFixed(3) + ' m';
            document.getElementById('calc-res-ymax').innerText = peak_y.toFixed(3) + ' m';
            document.getElementById('calc-res-vf').innerText = v_f.toFixed(3) + ' m/s';
        }
    </script>
</body>
</html>
"""

# 4. Streamlit 화면 렌더링 부
st.title("🪙 분수대에 동전 던지기 - 통합 시뮬레이터")
st.caption("30806 김성준 - 물리학 2 창의융합과제 설계 시뮬레이션 엔진 배포버전")

st.info("💡 초기 속도, 투사 각도, 그리고 출발지 고도를 조절하여 클래식 분수대 속에 동전을 골인시키는 물리학 실험 앱입니다. 학습 탭에서는 이론, 동적 그래프 변화, 계산기 가동이 모두 작동합니다.")

# 5. HTML 컴포넌트를 반응형으로 삽입
components.html(html_code, height=680, scrolling=True)
