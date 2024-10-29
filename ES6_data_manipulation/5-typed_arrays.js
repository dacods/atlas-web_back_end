export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);

  const bufferView = new DataView(buffer);

  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  bufferView.setInt8(position, value);

  return bufferView;
}
