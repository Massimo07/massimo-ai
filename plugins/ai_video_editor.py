"""
Modulo: ai_video_editor.py
Video editor AI: unisce clip, aggiunge logo/frase, musica. Pronto per generare reel, storie TikTok/IG, promo, onboarding personalizzato.
"""

import moviepy.editor as mpy

def create_promo_video(video_clips, logo_path, text, music_path, out="promo_final.mp4"):
    # video_clips: lista di file mp4
    clips = [mpy.VideoFileClip(v) for v in video_clips]
    final = mpy.concatenate_videoclips(clips)
    if logo_path:
        logo = (mpy.ImageClip(logo_path)
                .set_duration(final.duration)
                .resize(height=80)
                .set_position(("right", "bottom")))
        final = mpy.CompositeVideoClip([final, logo])
    if text:
        txt_clip = (mpy.TextClip(text, fontsize=48, color='white', font="Arial-Bold")
                    .set_position('center')
                    .set_duration(3))
        final = mpy.concatenate_videoclips([txt_clip, final])
    if music_path:
        audio = mpy.AudioFileClip(music_path)
        final = final.set_audio(audio)
    final.write_videofile(out, fps=24)
    return out

# --- ESEMPIO USO ---
# print(create_promo_video(["clip1.mp4", "clip2.mp4"], "logo.png", "Unisciti a Magic Team!", "music.mp3"))
