function SineWaveGenerator(options) {
  $.extend(this, options || {});

  if(!this.el) { throw "No Canvas Selected"; }
  this.ctx = this.el.getContext('2d');

  if(!this.waves.length) { throw "No waves specified"; }

  this._resizeWidth();
  window.addEventListener('resize', this._resizeWidth.bind(this));

  this.resizeEvent();
  window.addEventListener('resize', this.resizeEvent.bind(this));

  if(typeof this.initialize === 'function') {
    this.initialize.call(this);
  }

  this.loop();
}


SineWaveGenerator.prototype.speed = 10;
SineWaveGenerator.prototype.amplitude = 50;
SineWaveGenerator.prototype.wavelength = 50;
SineWaveGenerator.prototype.segmentLength = 10;

SineWaveGenerator.prototype.lineWidth = 2;
SineWaveGenerator.prototype.strokeStyle  = 'rgba(255, 255, 255, 0.2)';

SineWaveGenerator.prototype.resizeEvent = function() {};


SineWaveGenerator.prototype._resizeWidth = function() {
  this.dpr = window.devicePixelRatio || 1;

  this.width = this.el.width = window.innerWidth * this.dpr;
  this.height = this.el.height = window.innerHeight * this.dpr;
  this.el.style.width = window.innerWidth + 'px';
  this.el.style.height = window.innerHeight + 'px';

  this.waveWidth = this.width * 0.95;
  this.waveLeft = this.width * 0.25;
}

SineWaveGenerator.prototype.clear = function () {
  this.ctx.clearRect(0, 0, this.width, this.height);
}

SineWaveGenerator.prototype.time = 0;

SineWaveGenerator.prototype.update = function(time) {
  this.time = this.time - 0.005;
  if(typeof time === 'undefined') {
    time = this.time;
  }

  let index = -1;
  let length = this.waves.length;

  while(++index < length) {
    let timeModifier = this.waves[index].timeModifier || 1;
    this.drawSine(time * timeModifier, this.waves[index]);
  }

}


let PI2 = Math.PI * 2;
let HALFPI = Math.PI / 2;

SineWaveGenerator.prototype.ease = function(percent, amplitude) {
  return amplitude * (Math.sin(percent * PI2 - HALFPI) + 1) * 0.5;
}

SineWaveGenerator.prototype.drawSine = function(time, options) {
  options = options || {};
  let amplitude = options.amplitude || this.amplitude;
  let wavelength = options.wavelength || this.wavelength;
  let lineWidth = options.lineWidth || this.lineWidth;
  let strokeStyle = options.strokeStyle || this.strokeStyle;
  let segmentLength = options.segmentLength || this.segmentLength;

  let x = time;
  let y = 0;
  let amp = this.amplitude;

  let yAxis = this.height / 2;

  this.ctx.lineWidth = lineWidth * this.dpr;
  this.ctx.strokeStyle = strokeStyle;
  this.ctx.lineCap = 'round';
  this.ctx.lineJoin = 'round';
  this.ctx.beginPath();

  this.ctx.moveTo(0, yAxis);
  this.ctx.lineTo(this.waveLeft, yAxis);

  for(let i = 0; i < this.waveWidth; i += segmentLength) {
    x = (time * this.speed) + (-yAxis + i) / wavelength;
    y = Math.sin(x);

    amp = this.ease(i / this.waveWidth, amplitude);

    this.ctx.lineTo(i + this.waveLeft, amp * y + yAxis);

    amp = void 0;
  }

  this.ctx.lineTo(this.width, yAxis);

  this.ctx.stroke();
}

SineWaveGenerator.prototype.loop = function() {
  this.clear();
  this.update();

  window.requestAnimationFrame(this.loop.bind(this));
}

new SineWaveGenerator({
  el: document.getElementById('waves'),

  speed: 5,

  waves: [
    {
      timeModifier: 1,
      lineWidth: 8,
      amplitude: 150,
      wavelength: 200,
      segmentLength: 20,
      strokeStyle: 'rgba(255, 255, 255, 0.5)'
    },
    {
      timeModifier: 1.5,
      lineWidth: 2,
      amplitude: 250,
      wavelength: 200,
      strokeStyle: 'rgba(255, 255, 255, 0.3)'
    },
    {
      timeModifier: 1,
      lineWidth: 5,
      amplitude: -150,
      wavelength: 50,
      segmentLength: 10,
      strokeStyle: 'rgba(255, 255, 255, 0.2)'
    },
    {
      timeModifier: 0.5,
      lineWidth: 1.5,
      amplitude: -100,
      wavelength: 100,
      segmentLength: 20,
      strokeStyle: 'rgba(255, 255, 255, 0.1)'
    }
  ],

  initialize: function (){

  },

  resizeEvent: function() {
    let gradient = this.ctx.createLinearGradient(0, 0, this.width, 0);
    gradient.addColorStop(0,"rgba(0,0,0,0.01)");
    gradient.addColorStop(0.5,"rgba(255, 255, 255, 1)");
    gradient.addColorStop(1,"rgba(0,0,0,0.62)");

    let index = -1;
    let length = this.waves.length;
	  while(++index < length){
      this.waves[index].strokeStyle = gradient;
    }

  }

});