import pytest
from television import *

def test_init():
    tv=Television()
    assert str(tv)=='Power = False, Channel = 0, Volume = 0'

def test_power():
    tv=Television()
    tv.power()
    assert str(tv)=="Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv)=="Power = False, Channel = 0, Volume = 0"

def test_on_volume_then_mute():
    tv=Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv)=="Power = True, Channel = 0, Volume = 0"
def test_on_unmuted():
    tv=Television()
    tv.power()
    tv.mute()
    tv.mute()
    assert str(tv)=="Power = True, Channel = 0, Volume = 0"
def test_off_muted():
    tv=Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_off_unmuted():
    tv=Television()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_off_ch_up():
    tv=Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_on_ch_up():
    tv=Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
def test_on_ch_up_max():
    tv=Television()
    tv.power()
    tv.channel=Television.MAX_CHANNEL
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_off_ch_down():
    tv=Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_on_ch_down_min():
    tv=Television()
    tv.power()
    tv.channel=Television.MIN_CHANNEL
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_off_vol_up():
    tv=Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_on_vol_up():
    tv=Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
def test_on_muted_vol_up():
    tv=Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
def test_on_vol_up_max():
    tv=Television()
    tv.power()
    tv.volume=Television.MAX_VOLUME
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_off_vol_down():
    tv=Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
def test_on_vol_down():
    tv=Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
def test_on_muted_vol_down():
    tv=Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
def test_on_vol_down_min():
    tv=Television()
    tv.power()
    tv.volume=Television.MIN_VOLUME
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
