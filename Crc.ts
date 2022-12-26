function crc32(data: Uint8Array): number {

  let crc = 0xffffffff;

  for (let i = 0; i < data.length; i++) {

    crc ^= data[i];

    for (let j = 0; j < 8; j++) {

      if (crc & 1) {

        crc = (crc >>> 1) ^ 0xedb88320;

      } else {

        crc >>>= 1;

      }

    }

  }

  return crc ^ 0xffffffff;

}

// Example usage

const data = new Uint8Array([72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]);

const crc = crc32(data);

console.log(crc.toString(16));
