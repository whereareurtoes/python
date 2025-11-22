class Television:
    """
    A class representing details for a Television object.
    """

    """
    sets class variable constants
    """
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL=3

    def __init__(self, status:bool=False, muted:bool=False, volume:int=0, temp_volume:int=0, channel:int=0) -> None:
        """
        sets default values for television object
        """
        self.status=False
        self.muted=False
        self.volume=Television.MIN_VOLUME
        self.temp_volume=self.volume
        self.channel=Television.MIN_CHANNEL

    def power(self) -> None:
        """
        sets the power to on if off or off if on
        """
        if self.status:
            self.status=False
        else:
            self.status=True

    def mute(self) -> None:
        """
        if power on, sets volume to zero or returns past volume
        """
        if self.status:
            if self.muted:
                self.volume=self.temp_volume
                self.muted=False
            else:
                self.temp_volume=self.volume
                self.volume=0
                self.muted=True

    def channel_up(self) -> None:
        """
        if power on, increases channel by 1 or sets channel to 1 if at MAX_CHANNEL
        """
        if self.status:
            if self.channel==Television.MAX_CHANNEL:
                self.channel=Television.MIN_CHANNEL
            else:
                self.channel+=1

    def channel_down(self) -> None:
        """
        if power on, decreases channel by 1 or sets channel to 3 if at MIN_CHANNEL
        """
        if self.status:
            if self.channel==Television.MIN_CHANNEL:
                self.channel=Television.MAX_CHANNEL
            else:
                self.channel-=1

    def volume_up(self) -> None:
        """
        if power on, remove muted, increase volume by one if below MAX_VOLUME
        """
        if self.status:
            if self.muted:
                self.volume=self.temp_volume
                self.muted=False
            if self.volume<Television.MAX_VOLUME:
                self.volume+=1

    def volume_down(self) -> None:
        """
        if power on, remove muted, decrease volume by one if above MIN_VOLUME
        """
        if self.status:
            if self.muted:
                self.volume=self.temp_volume
                self.muted=False
            if self.volume>Television.MIN_VOLUME:
                self.volume-=1

    def __str__(self) -> str:
        """
        :return: power boolean, channel int, volume int
        """
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
