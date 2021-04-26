# author: kuangdd
# date: 2021/4/25
"""
### reference_audio
多个发音人的参考音频。
"""
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(Path(__file__).stem)

if __name__ == "__main__":
    logger.info(__file__)
    for line in sorted(Path(__file__).parent.glob('*')):
        print(line.name)
