# author: kuangdd
# date: 2021/4/25
"""
### audio
__init__.py
aliaudio-Aibao-000009.wav
aliaudio-Aicheng-000008.wav
aliaudio-Aida-000002.wav
aliaudio-Aijia-000005.wav
aliaudio-Aijing-000007.wav
aliaudio-Aimei-000007.wav
aliaudio-Aina-000008.wav
aliaudio-Aiqi-000007.wav
aliaudio-Aitong-000005.wav
aliaudio-Aiwei-000008.wav
aliaudio-Aixia-000005.wav
aliaudio-Aiya-000005.wav
aliaudio-Aiyu-000005.wav
aliaudio-Aiyue-000008.wav
aliaudio-Siyue-000005.wav
aliaudio-Xiaobei-000008.wav
aliaudio-Xiaogang-000005.wav
aliaudio-Xiaomei-000008.wav
aliaudio-Xiaomeng-000008.wav
aliaudio-Xiaowei-000008.wav
aliaudio-Xiaoxue-000008.wav
aliaudio-Xiaoyun-000001.wav
aliaudio-Yina-000008.wav
biaobei-biaobei-009502.mp3
cctv-cctvfa-cctv-20191212-022-011.mp3
cctv-cctvfb-cctv-20200111-013-002.mp3
cctv-cctvma-cctv-20191201-002-006.mp3
cctv-cctvmb-cctv-20200111-001-002.mp3
cctv-cctvmc-cctv-20200111-001-015.mp3
cctv-cctvmd-cctv-20191214-002-052.mp3

index-speaker-map:
{1: 'Aibao', 2: 'Aicheng', 3: 'Aida', 4: 'Aijia', 5: 'Aijing', 6: 'Aimei', 7: 'Aina', 8: 'Aiqi', 9: 'Aitong', 10: 'Aiwei',
11: 'Aixia', 12: 'Aiya', 13: 'Aiyu', 14: 'Aiyue', 15: 'Siyue', 16: 'Xiaobei', 17: 'Xiaogang', 18: 'Xiaomei', 19: 'Xiaomeng', 20: 'Xiaowei',
21: 'Xiaoxue', 22: 'Xiaoyun', 23: 'Yina', 24: 'biaobei', 25: 'cctvfa', 26: 'cctvfb', 27: 'cctvma', 28: 'cctvmb', 29: 'cctvmc', 30: 'cctvmd'}
"""
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(Path(__file__).stem)

_audio_list = '''aliaudio-Aibao-000009.wav
aliaudio-Aicheng-000008.wav
aliaudio-Aida-000002.wav
aliaudio-Aijia-000005.wav
aliaudio-Aijing-000007.wav
aliaudio-Aimei-000007.wav
aliaudio-Aina-000008.wav
aliaudio-Aiqi-000007.wav
aliaudio-Aitong-000005.wav
aliaudio-Aiwei-000008.wav
aliaudio-Aixia-000005.wav
aliaudio-Aiya-000005.wav
aliaudio-Aiyu-000005.wav
aliaudio-Aiyue-000008.wav
aliaudio-Siyue-000005.wav
aliaudio-Xiaobei-000008.wav
aliaudio-Xiaogang-000005.wav
aliaudio-Xiaomei-000008.wav
aliaudio-Xiaomeng-000008.wav
aliaudio-Xiaowei-000008.wav
aliaudio-Xiaoxue-000008.wav
aliaudio-Xiaoyun-000001.wav
aliaudio-Yina-000008.wav
biaobei-biaobei-009502.mp3
cctv-cctvfa-cctv-20191212-022-011.mp3
cctv-cctvfb-cctv-20200111-013-002.mp3
cctv-cctvma-cctv-20191201-002-006.mp3
cctv-cctvmb-cctv-20200111-001-002.mp3
cctv-cctvmc-cctv-20200111-001-015.mp3
cctv-cctvmd-cctv-20191214-002-052.mp3'''.split('\n')

_speaker_list = [w.split('-')[1] for w in _audio_list]

if __name__ == "__main__":
    logger.info(__file__)
    for line in sorted(Path(__file__).parent.glob('*')):
        print(line.name)
    print({i: w for i, w in enumerate(_speaker_list, 1)})
