#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import time
from datetime import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT

def demo():
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")        
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial)
    print('cool')
    msg = dt_string
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.05)
    time.sleep(0.5)



