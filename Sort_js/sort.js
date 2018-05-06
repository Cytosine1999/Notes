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

Element.prototype.fill = function(m, n) {
	var cord = this.getXY(m, n);
	this.fillXY(cord.x, cord.y);
};

Element.prototype.fillXY = function(x, y) {
	ctx.fillRect(x, y, length, length);
	setColor("white");
	ctx.fillText(this.value, x + this.hl, y + this.hl);
};

Element.prototype.clear = function(m, n) {
	var cord = this.getXY(m, n);
	ctx.clearRect(cord.x - 1, cord.y - 1, length + 2, length + 2);
}

Element.prototype.move = function(m1, n1, m2, n2) {
	
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
	this.status;
	var sup = size << 2;
	for (i = 0; i < size; i++) {
		this.data[i] = new Element(Math.floor(Math.random() * sup));
	}
}

Data.prototype.md = margin + distance;
Data.prototype.m2d = Data.prototype.md + margin;
Data.prototype.dl = distance + length;

Data.prototype.swap = function(a, b, c) {
	if (b == c) {
		var tmp = this.data[b];
		this.data[b] = this.data[a];
		this.data[a] = tmp;
	} else {
		var tmp = this.data[c];
		this.data[c] = this.data[b];
		this.data[b] = this.data[a];
		this.data[a] = tmp;
	}
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
	var size = last.end - last.begin;

	if (this.status != undefined) {
		this.drawFocus();
		if (this.status.i == this.data.length) {
			this.stack.push({
				begin: last.begin,
				end: this.status.flag,
				left: true
			});
			this.status = undefined;
			return;
		}
		while (this.status.i < this.data.length) {
			if (this.data[this.status.i] < this.data[this.status.flag]) {
				this.swap(this.status.flag, this.status.flag + 1, this.status.i);
				this.status.flag ++;
				this.status.i ++;
				return;
			}
			this.status.i ++;
		}
		return;
	}

	if (size > 1) {
		this.drawOther();
		this.status = {
			i: last.begin + 1,
			flag: last.begin,
		}
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
	}
	this.quickSort();
};

function ArgColor(start, color) {
	return {
		start: start,
		color: color
	};
}

Data.prototype.toCord = function(i) {
	var n = Math.floor(focus.begin / this.line);
	var m = focus.begin - n * this.line;
	return {
		n: n,
		m: m
	}
}

Data.prototype.refresh = function(color, args) {
	this.line = Math.floor((frame.width - this.m2d) / this.dl);
	this.row = Math.ceil(this.data.length / this.line);
	frame.height = this.m2d + this.row * this.dl;
	setColor(color);
	var flag = 0;
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

Data.prototype.drawOther = function() {
	var last = this.stack[this.stack.length - 1];
	var lastLast = this.stack[this.stack.length - 2];
	if (this.stack.length > 1) {
		var args = [];
		if (last.left) {
			args.push(ArgColor(last.begin, "white"));
			args.push(ArgColor(last.end, "black"));
			args.push(ArgColor(last.end + 1, "red"));
			args.push(ArgColor(lastLast.end, "gray"));
		} else {
			args.push(ArgColor(last.begin - 1, "black"));
			args.push(ArgColor(last.begin, "white"));
			args.push(ArgColor(last.end, "gray"));
		}
		this.refresh ("green", args);
		this.strokeElement(lastLast.begin, lastLast.end, "gray");
	} else {
		this.refresh ("white", []);
	}
	this.strokeElement(last.begin, last.end, "black");
}

Data.prototype.drawFocus = function() {
	var focus = this.stack[this.stack.length - 1];
	var flag = this.data[this.status.flag];
	var n = Math.floor(focus.begin / this.line);
	var m = focus.begin - n * this.line;
	for (i = focus.begin; i < focus.end; i++) {
		if (this.data[i] > flag) {
			setColor("red");
		} else if (this.data[i] < flag) {
			setColor("green");
		} else {
			setColor("black");
		}
		this.data[i].fill(m, n);
		m ++;
		if (m == this.line) {
			m = 0;
			n ++;
		}
	}
}

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
