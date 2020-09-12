function dft(samples, amount) {
  var len = samples.length;
  var arr = Array(len);
  var invlen = 1 / len;
  for (var i = 0; i < amount; i++) {
    arr[i] = createComplex(0, 0);
    for (var n = 0; n < len; n++) {
      var theta = pi2 * i * n * invlen;
      var costheta = Math.cos(theta);
      var sintheta = Math.sin(theta);
      arr[i].re += samples[n].re * costheta - samples[n].im * sintheta;
      arr[i].im += samples[n].re * sintheta + samples[n].im * costheta;
    }
  }
  return arr;
}