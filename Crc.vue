<template>

  <div>

    <p>CRC: {{ crc }}</p>

  </div>

</template>

<script>

  import { ref } from 'vue';

  export default {

    setup() {

      const crc = ref(null);

      function calculateCrc(data) {

        let crcValue = 0xffffffff;

        for (let i = 0; i < data.length; i++) {

          crcValue ^= data[i];

          for (let j = 0; j < 8; j++) {

            if (crcValue & 1) {

              crcValue = (crcValue >>> 1) ^ 0xedb88320;

            } else {

              crcValue >>>= 1;

            }

          }

        }

        return crcValue ^ 0xffffffff;

      }

      const data = new Uint8Array([72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]);

      crc.value = calculateCrc(data).toString(16);

      return { crc };

    }

  }

</script>
