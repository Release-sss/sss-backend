import express from "express";
import dotenv from "dotenv";

import { routes } from "./routes.js";

dotenv.config();

const app = express();
app.listen(process.env.PORT, () => {
  console.log(`server has started on port ${process.env.PORT}`);
});

routes.forEach(({ basePath, controller }) => {
  app.use(basePath, controller);
});
