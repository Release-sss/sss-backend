export class ContentLengthDoesNotExist extends Error {
  constructor(message: string) {
    super();
    this.message = message;
  }
}
