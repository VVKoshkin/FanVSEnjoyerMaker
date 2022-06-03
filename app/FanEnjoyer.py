from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import logging

logging.basicConfig(level=logging.INFO)


class FanEnjoyer:

    orig_path = 'template.mp4'

    def __init__(self, fan_text, enjoyer_text):
        logging.info('Init FanEnjoyer object')
        self.fan_text = fan_text
        self.enjoyer_text = enjoyer_text
        self.clip = VideoFileClip(self.orig_path)

    def make(self):
        try:
            logging.info('Setting text...')
            self.fan_text = f'Average\n{self.fan_text}\nfan'
            self.enjoyer_text = f'Average\n{self.enjoyer_text}\nenjoyer'
            txt_clip_fan = TextClip(txt=self.fan_text, fontsize=20, color='black')
            txt_clip_enjoyer = TextClip(txt=self.enjoyer_text, fontsize=20, color='black')
            # positioning TODO maybe I can align it automatically?
            pos_test_fan = (60, 0)
            pos_test_enjoyer = (300, 0)
            # position setting for texts
            txt_clip_fan = txt_clip_fan.set_pos(pos_test_fan)
            txt_clip_enjoyer = txt_clip_enjoyer.set_pos(pos_test_enjoyer)
            duration = self.clip.duration
            res_path = 'result.mp4'
            video = CompositeVideoClip([self.clip, txt_clip_fan, txt_clip_enjoyer])
            video.duration = duration
            video.write_videofile(res_path)
            return 0
        except:
            return -1


def test_it():
    maker = FanEnjoyer('новопассит', 'галоперидол')
    result = maker.make()
    if result != 0:
        logging.error('Чёто пошло не так')
    else:
        logging.info('Всё ок файл готов!')


