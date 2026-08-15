class NetCapitalGainLoss:
    """
    Performs the netting process for capital gains and losses per
    US Federal Taxation rules (short-term vs. long-term).

    Convention: gains are entered as positive numbers (or 0),
    losses are entered as negative numbers (or 0).
    """

    def __init__(self, st_gains, st_losses, lt_gains, lt_losses):
        if st_losses > 0 or lt_losses > 0:
            raise ValueError("Losses must be entered as negative numbers (or zero).")
        if st_gains < 0 or lt_gains < 0:
            raise ValueError("Gains must be entered as positive numbers (or zero).")

        self.st_gains = st_gains
        self.st_losses = st_losses
        self.lt_gains = lt_gains
        self.lt_losses = lt_losses
        self.net = {
            "Net ST": 0,
            "Net LT": 0,
            "Overall": 0,
            "Character": ""
        }

    def netting_process(self):
        net_st = self.st_gains + self.st_losses
        net_lt = self.lt_gains + self.lt_losses
        overall = net_st + net_lt

        self.net["Net ST"] = net_st
        self.net["Net LT"] = net_lt
        self.net["Overall"] = overall

        if net_st == 0 and net_lt == 0:
            self.net["Character"] = "None"
        elif net_st >= 0 and net_lt >= 0:
            # Same sign (or one side is exactly zero): nothing offsets,
            # both sides keep their own character.
            self.net["Character"] = "Net Short-term and Long-term Capital Gain"
        elif net_st <= 0 and net_lt <= 0:
            self.net["Character"] = "Net Short-term and Long-term Capital Loss"
        else:
            # Opposite signs: whichever side has the bigger magnitude
            # determines the overall character. overall's own sign
            # already tells us who won, so no extra abs() comparison needed.
            if overall == 0:
                self.net["Character"] = "None"
            elif overall > 0:
                self.net["Character"] = (
                    "Net Short-term Capital Gain" if net_st > 0 else "Net Long-term Capital Gain"
                )
            else:
                self.net["Character"] = (
                    "Net Short-term Capital Loss" if net_st < 0 else "Net Long-term Capital Loss"
                )

        return self.net
