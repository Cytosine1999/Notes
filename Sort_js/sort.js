var size = 50;
var data;
var form = document.getElementById("form");
var frame = document.getElementById("frame");
var sort = document.getElementById("sort");
var ctx = frame.getContext("2d");

var margin = 6;
var distance = 6;
var length = 40;

function setColor(color) {
	ctx.font = "bold 12pt sans-serif";
	ctx.textAlign = "center";
	ctx.textBaseline = "middle";
	ctx.fillStyle = color;
	ctx.strokeStyle = color;
}

function Element(value) {
	this.value = value;
}

Element.prototype.dl = distance + length;
Element.prototype.md = margin + distance;
Element.prototype.hl = length / 2;
Element.prototype.ld2 = length - 2;

Element.prototype.toString = function() {
	return this.value.toString();
};

Element.prototype.valueOf = function() {
	return this.value;
};

Element.prototype.getXY = function(m, n) {
	return {
		x: this.md + m * this.dl,
		y: this.md + n * this.dl
	}
}

Element.prototype.draw = function(m, n) {
	var cord = this.getXY(m, n);
	this.drawXY(cord.x, cord.y);
};

Element.prototype.drawXY = function(x, y) {
	ctx.strokeRect(x, y, length, length);
	ctx.fillText(this.value, x + this.hl, y + this.hl);
};

function Data(size) {
	this.data = Array(size);
	this.line;
	this.row;
	this.stack = Array({
		begin: 0, 
		end: size, 
		left: false
	});
	this.id;
	var sup = size << 2;
	for (i = 0; i < size; i++) {
		this.data[i] = new Element(Math.floor(Math.random() * sup));
	}
}

Data.prototype.md = margin + distance;
Data.prototype.m2d = Data.prototype.md + margin;
Data.prototype.dl = distance + length;

Data.prototype.compare = function(a, b) {
	return this.data[a] < this.data[b];
};

Data.prototype.swap = function(a, b, c) {
	var tmp = this.data[c];
	this.data[c] = this.data[b];
	this.data[b] = this.data[a];
	this.data[a] = tmp;
};

Data.prototype.stopSort = function() {
	window.clearInterval(this.id);
	if (this.id != undefined) {
		this.id = undefined;
		sort.disabled = false;
	}
}

Data.prototype.quickSort = function() {
	if (this.stack.length == 0) {
		this.stopSort();
		window.onresize = resizeCanvas;
		setTimeout("resizeCanvas();", 1000);
		return;
	}
	var last = this.stack[this.stack.length - 1];
	var lastLast = this.stack[this.stack.length - 2];
	var size = last.end - last.begin;
	if (size > 1) {
		if (this.stack.length > 1) {
			var args = [];
			if (last.left) {
				args.push(ArgColor(last.begin, "black"));
				args.push(ArgColor(last.end, "red"));
				args.push(ArgColor(last.end + 1, "blue"));
				args.push(ArgColor(lastLast.end, "gray"));
			} else {
				args.push(ArgColor(last.begin - 1, "red"));
				args.push(ArgColor(last.begin, "black"));
				args.push(ArgColor(last.end, "gray"));
			}
			this.refresh ("green", args);
			this.strokeElement(lastLast.begin, lastLast.end, "gray");
		} else {
			this.refresh ("black", []);
		}
		this.strokeElement(last.begin, last.end, "black");
		var flag = last.begin;
		for (i = last.begin + 1; i < last.end; i++) {
			if (this.compare(i, flag)) {
				this.swap(flag, flag + 1, i);
				flag ++;
			}
		}
		this.stack.push({
			begin: last.begin,
			end: flag,
			left: true
		});
	} else {
		var tmp;
		do {
			tmp = this.stack.pop();
		} while (tmp != undefined && !tmp.left);
		if (this.stack.length > 0) {
			this.stack.push({
				begin: tmp.end + 1,
				end: this.stack[this.stack.length - 1].end,
				left: false
			});
		}
		this.quickSort();
	}
};

function ArgColor(start, color) {
	return {
		start: start,
		color: color
	};
}

Data.prototype.refresh = function(color, args) {
	this.line = Math.floor((frame.width - this.m2d) / this.dl);
	this.row = Math.ceil(this.data.length / this.line);
	frame.height = this.m2d + this.row * this.dl;
	setColor(color);
	flag = 0;
	var i = 0;
	for (n = 0; n < this.row; n++) {
		for (m = 0; m < this.line; m++) {
			if (i == this.data.length) {
				return;
			}
			if (args.length > flag) {
				while(args.length > flag && args[flag].start <= i) {
					if (args[flag].start == i) {
						setColor(args[flag].color);
					}
					flag++;
				}
			}
			this.data[i].draw(m, n);
			i ++;
		}
	}
};

Data.prototype.strokeElement = function(begin, end, color) {
	bn = Math.floor(begin / this.line);
	bm = begin - bn * this.line;
	en = Math.floor(end / this.line);
	em = end - en * this.line;
	if (em == 0 && en > 0) {
		en --;
		em = this.line;
	}
	if ((en - bn) == 1 && em < bm) {
		var cut = en * this.line;
		this.strokeElement(begin, cut, color);
		this.strokeElement(cut, end, color);
	} else if (en == bn) {
		var cord = Element.prototype.getXY(bm, bn);
		ctx.strokeStyle = color;
		ctx.strokeRect(cord.x - 2, cord.y - 2, (em - bm) * this.dl - distance + 4, length + 4);
	} else {
		bxy = Element.prototype.getXY(bm, bn);
		bxy.x -= 2;
		bxy.y -= 2;
		exy = Element.prototype.getXY(em, en);
		exy.x -= distance - 2;
		exy.y += 2 + length;
		bx = this.md - 2;
		by = bxy.y + this.dl;
		rx = this.line * this.dl + margin + 2;
		ry = exy.y - this.dl;
		ctx.strokeStyle = color;
		ctx.beginPath();
		ctx.moveTo(bx, by);
		ctx.lineTo(bxy.x, by);
		ctx.lineTo(bxy.x, bxy.y);
		ctx.lineTo(rx, bxy.y);
		ctx.lineTo(rx, ry);
		ctx.lineTo(exy.x, ry);
		ctx.lineTo(exy.x, exy.y);
		ctx.lineTo(bx, exy.y);
		ctx.closePath();
		ctx.stroke();
	}
}

function resizeCanvas() {
	frame.width = window.innerWidth - 16;
	if (data.stack.length == 0) {
		data.refresh("green", []);
	} else {
		data.refresh("black", []);
	}
	
}

window.onresize = resizeCanvas;

function getValue(event) {
	event = EventUtil.getEvent(event);
	EventUtil.preventDefault(event);
	size = form.elements["size"].value;
	data.stopSort();
	data = new Data(size);
	resizeCanvas();
}

function sortData() {
	data.id = setInterval('data.quickSort()', 1000);
	sort.disabled = true;
	window.onresize = null;
}

data = new Data(size);
resizeCanvas();
EventUtil.addHandler(form, "submit", getValue);
