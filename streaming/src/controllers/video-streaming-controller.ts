import { Router } from "express";
import got from "got";

import {
  getChunkProps,
  getContentLength,
} from "../services/video-streaming-service.js";

export const videoStreamingController = Router();

videoStreamingController.get("/", async (req, res) => {
  const key = req.query.key;
  const url = encodeURI(`https://flit.s3.ap-northeast-2.amazonaws.com/${key}`);

  try {
    const contentLength = await getContentLength(url);

    const requestRangeHeader = req.headers.range;

    if (!requestRangeHeader) {
      got.stream(url, { isStream: true }).pipe(res);
      return;
    }

    const { start, end, chunkSize } = getChunkProps(
      requestRangeHeader,
      contentLength
    );

    res.writeHead(206, {
      "Content-Range": `bytes ${start}-${end}/${contentLength}`,
      "Accept-Ranges": "bytes",
      "Content-Length": chunkSize,
      "Content-Type": "video/mp4",
    });
  } catch (err) {
    res.statusCode = 400;
    res.end();
    return;
  }

  try {
    got
      .stream(url, {
        isStream: true,
        headers: {
          ...req.headers,
          host: "flit.s3.ap-northeast-2.amazonaws.com",
          referer: url,
        },
      })
      .pipe(res);
  } catch (err) {
    console.log(err);
  }
});
