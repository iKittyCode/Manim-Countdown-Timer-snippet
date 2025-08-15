
def CountdownTimer(self, seconds, color):
        start_time = seconds


        timer_display = DecimalNumber(
            start_time,
            num_decimal_places=0,
            include_sign=False
        ).scale(2)
        timer_display.to_edge(UP)


        def update_timer(mobj, dt):
            mobj.set_value(max(0, mobj.get_value() - dt))

        timer_display.add_updater(update_timer)
        self.add(timer_display)


        self.wait(start_time)


        timer_display.remove_updater(update_timer)


        self.play(Flash(timer_display))
        self.play(timer_display.animate.set_color(color))
