from source.mission.template.mission_just_collect import MissionJustCollectGroup
META={
    'name':{
        'zh_CN':'采集塞西莉亚花',
        'en_US':'Collect Cecilia'
    }
}
class MissionJueyunChili(MissionJustCollectGroup):
    def __init__(self):
        super().__init__(['JueyunChili20230513212046i0',
                          'JueyunChili20230513212310i0'
                          ],
                           name='MissionJueyunChili')

if __name__ == '__main__':
    import time
    MissionJueyunChili().start()
    while 1:time.sleep(1)