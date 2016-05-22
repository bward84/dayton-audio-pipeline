#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Notch
# Generated: Sun May 22 10:21:16 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class notch(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Notch")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 16000

        ##################################################
        # Blocks
        ##################################################
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/bward/Documents/Labhack 2016/Initial Audio Files/Dayton Fire Department/454 E Fifth St/PCM/Recorded on 19-Feb-2009 at 18.57.33 (-AI8Q#5D02357272).WAV", False)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/bward/Documents/Labhack 2016/Cleaned Audio/cleaned_audio.wav", 1, samp_rate, 16)
        self.band_reject_filter_0 = filter.fir_filter_fff(1, firdes.band_reject(
        	1, samp_rate, 1000, 1050, 10, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_reject_filter_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_reject_filter_0, 0))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, 1000, 1050, 10, firdes.WIN_HAMMING, 6.76))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = notch()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()