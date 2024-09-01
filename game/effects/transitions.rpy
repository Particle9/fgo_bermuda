
init:
    image black:
        Solid("#000")
    image white:
        Solid("#FFF")

    image effect eye_blink:
        "effects/eye.png"
        xsize 1920
        ysize 1080

    image effect dream:
        "effects/dream.png"
        xsize 1920
        ysize 1080

    image effect teleport:
        "effects/teleport.png"
        xsize 1920
        ysize 1080

    python:
        def eyewarp(x):
            return x**1.33
        eye_open = ImageDissolve("effect eye_blink", .5, ramplen=128, reverse=False, time_warp=eyewarp)
        eye_shut = ImageDissolve("effect eye_blink", .5, ramplen=128, reverse=True, time_warp=eyewarp)

        flash = Fade(.25, 0, .75, color="#fff")

        dream = ImageDissolve("effect dream", 1.0, 0)

        teleport = ImageDissolve("effect teleport", 2.0, 64)


