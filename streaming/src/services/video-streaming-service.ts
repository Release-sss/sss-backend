import got from "got";

import { ContentLengthDoesNotExist } from "./errors.js";

export const getContentLength = async (url: string): Promise<number> => {
  try {
    const res = await got.head(url);
    return Number(res.headers["content-length"]);
  } catch (err) {
    throw new ContentLengthDoesNotExist(String(err));
  }
};

export const getChunkProps = (range: string, fileSize: number) => {
  const parts = range.replace(/bytes=/, "").split("-");

  const start = parseInt(parts[0], 10);
  const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;
  const chunkSize = end - start + 1;

  return {
    start,
    end,
    chunkSize,
  };
};
