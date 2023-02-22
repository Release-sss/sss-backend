import { videoStreamingController } from "./controllers/video-streaming-controller.js";

export const routes = [
  {
    basePath: "/video",
    controller: videoStreamingController,
  },
];
