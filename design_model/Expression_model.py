#-*- coding:utf-8 -*-
"""
 解释器模式
"""
class PlayContext():
    play_text=None

class Expression():
    # 负责转译谱
    def interpret(self,context):
        if len(context.play_text)==0:
            return
        else:
            play_segs=context.play_text.split(' ')
            for play_seg in play_segs:
                pos=0
                for ele in play_seg:
                    if ele.isalpha():
                        pos+=1
                        continue
                    break

                play_chord=play_seg[0:pos]
                play_value=play_seg[pos:]
                self.execute(play_chord,play_value)
    # 负责演奏
    def execute(self,play_key,play_value):
        pass

class NormGuitar(Expression):
    def execute(self,key,value):
        print ('Normal Guitar Playing--Chord:%s Play Tune:%s'%(key,value))

if __name__ == '__main__':
    context=PlayContext()
    context.play_text='C53231323 Em43231323 F43231323 G63231323'
    guitar=NormGuitar()
    guitar.interpret(context)