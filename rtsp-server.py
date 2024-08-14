#!/usr/bin/env python3
# Required packages installation:
# sudo apt-get install gstreamer1.0-tools gstreamer1.0-rtsp gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
# sudo apt-get install libcairo2 libcairo2-dev pkg-config
# sudo apt-get install libgirepository1.0-dev gir1.2-gstreamer-1.0 gobject-introspection

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject

class RtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self, **properties):
        super(RtspMediaFactory, self).__init__(**properties)
        self.set_launch(
            "( filesrc location=sample.mp4 loop=true ! qtdemux name=demux demux.video_0 ! decodebin ! videoconvert ! x264enc tune=zerolatency ! rtph264pay name=pay0 pt=96 )"
        )
        self.set_shared(True)

class RtspServer(GstRtspServer.RTSPServer):
    def __init__(self, **properties):
        super(RtspServer, self).__init__(**properties)
        self.factory = RtspMediaFactory()
        self.get_mount_points().add_factory("/test", self.factory)
        self.attach(None)

def main():
    Gst.init(None)

    # Create and start the RTSP server
    server = RtspServer()

    loop = GObject.MainLoop()
    print("RTSP server is running at rtsp://127.0.0.1:8554/test")
    loop.run()

if __name__ == "__main__":
    GObject.threads_init()
    main()
