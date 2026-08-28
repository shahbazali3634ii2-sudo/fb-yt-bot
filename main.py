from flask import Flask, render_template_string, request

app = Flask(__name__)

# Complete Cyber Hacker Aesthetic Mobile UI Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CYBER.AUTO_BOT</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #0b0f19; color: #e2e8f0; font-family: monospace; }
        .cyber-box { background: #131c2e; border: 1px solid #1e3a8a; box-shadow: 0 0 15px rgba(30, 58, 138, 0.3); }
        .cyber-btn { background: linear-gradient(to right, #4f46e5, #9333ea); }
        .cyber-btn:hover { opacity: 0.9; }
    </style>
</head>
<body class="flex justify-center items-center min-h-screen p-2">

    <!-- Mobile Device Container (9:16 Aspect Look) -->
    <div class="w-full max-w-md cyber-box rounded-2xl p-4 flex flex-col justify-between space-y-4">
        
        <!-- Header -->
        <div class="flex justify-between items-center border-b border-blue-900 pb-2">
            <h1 class="text-lg font-bold text-cyan-400">🤖 CYBER.AUTO_BOT</h1>
            <span class="text-xs bg-blue-900 text-cyan-200 px-2 py-0.5 rounded">AUTO</span>
        </div>

        <form action="/publish" method="POST" class="space-y-4">
            
            <!-- STEP 1: VIDEO LINK -->
            <div class="cyber-box p-3 rounded-xl space-y-2">
                <label class="text-xs text-cyan-300 font-bold">[ STEP 1: VIDEO LINK ]</label>
                <p class="text-xs text-gray-400">Enter YouTube Video URL:</p>
                <input type="text" name="youtube_url" placeholder="https://youtube.com/watch?v=..." required 
                       class="w-full bg-slate-900 border border-slate-700 rounded p-2 text-xs text-white focus:outline-none focus:border-cyan-500">
            </div>

            <!-- STEP 2: SELECT & CONNECT PLATFORMS -->
            <div class="cyber-box p-3 rounded-xl space-y-2">
                <label class="text-xs text-cyan-300 font-bold">[ STEP 2: SELECT TARGET PLATFORM ]</label>
                <div class="grid grid-cols-1 gap-2">
                    <button type="submit" name="action" value="tiktok" class="w-full bg-slate-900 border border-pink-600 text-pink-400 text-xs py-2 rounded font-bold hover:bg-pink-950 transition">🎵 Continue with TikTok</button>
                    <button type="submit" name="action" value="facebook" class="w-full bg-slate-900 border border-blue-600 text-blue-400 text-xs py-2 rounded font-bold hover:bg-blue-950 transition">📘 Continue with Facebook</button>
                    <button type="submit" name="action" value="instagram" class="w-full bg-slate-900 border border-purple-600 text-purple-400 text-xs py-2 rounded font-bold hover:bg-purple-950 transition">📸 Continue with Instagram</button>
                    <button type="submit" name="action" value="youtube" class="w-full bg-slate-900 border border-red-600 text-red-400 text-xs py-2 rounded font-bold hover:bg-red-950 transition">🔴 Continue with YouTube</button>
                </div>
                <button type="submit" name="action" value="all" class="w-full mt-2 cyber-btn text-white text-xs py-2.5 rounded font-bold tracking-wide">🚀 LOG IN TO ALL PLATFORMS</button>
            </div>

            <!-- STEP 3: AUTOMATION & SCHEDULING SETTINGS -->
            <div class="cyber-box p-3 rounded-xl space-y-3">
                <label class="text-xs text-cyan-300 font-bold">[ STEP 3: FORMAT & SCHEDULE ]</label>
                
                <!-- Auto Schedule Time Picker -->
                <div class="flex justify-between items-center bg-slate-900 p-2 rounded border border-slate-700">
                    <span class="text-xs text-gray-300">⏱️ Upload Time:</span>
                    <input type="time" name="schedule_time" value="07:00" class="bg-slate-800 text-cyan-300 text-xs p-1 rounded border border-slate-600">
                </div>

                <!-- Reel vs Long Format Toggle -->
                <div class="flex justify-between items-center bg-slate-900 p-2 rounded border border-slate-700">
                    <span class="text-xs text-gray-300">🎬 Video Format:</span>
                    <div class="flex items-center space-x-2">
                        <span class="text-[10px] text-cyan-400 font-bold">REEL</span>
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" name="video_format" value="long" class="sr-only peer">
                            <div class="w-9 h-5 bg-slate-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-blue-600"></div>
                        </label>
                        <span class="text-[10px] text-gray-400 font-bold">LONG</span>
                    </div>
                </div>

                <!-- Features info -->
                <div class="text-[10px] text-gray-400 space-y-1 pt-1 border-t border-slate-800">
                    <p>✨ <b>AI Engine:</b> Auto-generates Optimized Titles & Hashtags</p>
                    <p>🛡️ <b>Quality & Safety:</b> HD Edit & Non-Copyright Bypass Active</p>
                </div>
            </div>

            <!-- FINAL PUBLISH ACTION BUTTON -->
            <button type="submit" name="action" value="publish" class="w-full cyber-btn text-white text-sm py-3 rounded-xl font-extrabold shadow-lg tracking-wider">
                🚀 PUBLISH REELS
            </button>

        </form>

        <!-- Footer Nav -->
        <div class="flex justify-around text-[10px] text-gray-400 border-t border-blue-900 pt-2">
            <span class="text-cyan-400 font-bold">Dashboard</span>
            <span>History</span>
            <span>Schedule</span>
            <span>Settings</span>
        </div>

    </div>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/publish', methods=['POST'])
def publish():
    youtube_url = request.form.get('youtube_url')
    action = request.form.get('action')
    schedule_time = request.form.get('schedule_time')
    video_format = request.form.get('video_format')
    
    format_type = "Long Video (16:9)" if video_format == 'long' else "Reel / Short (9:16)"
    
    return f"""
    <body style="background:#0b0f19; color:#fff; font-family:monospace; padding:20px;">
        <h2>⚡ Pipeline Triggered Successfully!</h2>
        <p><b>Target Action:</b> {action.upper()}</p>
        <p><b>YouTube Source:</b> {youtube_url}</p>
        <p><b>Selected Format:</b> {format_type}</p>
        <p><b>Scheduled Upload Time:</b> {schedule_time}</p>
        <p style="color:#00ff00;">[STATUS] AI generating title, tags & applying HD non-copyright processing...</p>
        <br>
        <a href="/" style="color:cyan; text-decoration:underline;">← Back to Dashboard</a>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
