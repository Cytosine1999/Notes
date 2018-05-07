let size = 50;
let data;
let form = document.getElementById("form");
let frame = document.getElementById("frame");
let sort = document.getElementById("sort");
let ctx = frame.getContext("2d");

const margin = 6;
const distance = 6;
const length = 40;

function Element(value) {
    this.value = value;
}

Element.prototype.dl = distance + length;
Element.prototype.md = margin + distance;
Element.prototype.hl = length / 2;

Element.prototype.toString = function () {
    return this.value.toString();
};

Element.prototype.valueOf = function () {
    return this.value;
};

Element.prototype.getXY = function (m, n) {
    return {
        x: this.md + m * this.dl,
        y: this.md + n * this.dl
    }
};

Element.prototype.draw = function (m, n) {
    let cord = this.getXY(m, n);
    this.drawXY(cord.x, cord.y);
};

Element.prototype.drawXY = function (x, y) {
    ctx.strokeRect(x, y, length, length);
    ctx.fillText(this.value, x + this.hl, y + this.hl);
};

Element.prototype.fill = function (m, n) {
    let cord = this.getXY(m, n);
    this.fillXY(cord.x, cord.y);
};

Element.prototype.fillXY = function (x, y) {
    ctx.fillRect(x, y, length, length);
    setColor("white");
    ctx.fillText(this.value, x + this.hl, y + this.hl);
};

Element.prototype.clear = function (m, n) {
    let cord = this.getXY(m, n);
    ctx.clearRect(cord.x - 1, cord.y - 1, length + 2, length + 2);
};

function Data(size) {
    this.data = Array(size);
    this.line = undefined;
    this.row = undefined;
    this.stack = Array({
        begin: 0,
        end: size,
        left: false
    });
    this.id = undefined;
    this.moveId = undefined;
    this.status = undefined;
    let sup = size << 2;
    for (let i = 0; i < size; i++) {
        this.data[i] = new Element(Math.floor(Math.random() * sup));
    }
}

Data.prototype.md = margin + distance;
Data.prototype.m2d = Data.prototype.md + margin;
Data.prototype.dl = distance + length;

Data.prototype.swap = function (a, b, c) {
    let tmp = this.data[c];
    this.data[c] = this.data[b];
    this.data[b] = this.data[a];
    this.data[a] = tmp;
};

Data.prototype.stopSort = function () {
    if (this.id !== undefined) {
        window.clearInterval(this.id);
        window.clearInterval(this.moveId);
        window.onresize = resizeCanvas;
        this.id = undefined;
        sort.disabled = false;
    }
};

Data.prototype.quickSort = function () {
    if (this.stack.length === 0) {
        this.stopSort();
        setTimeout("resizeCanvas();", 1000);
        return;
    }
    let last = this.stack[this.stack.length - 1];
    let size = last.end - last.begin;
    if (this.status !== undefined) {
        this.drawOther();
        this.drawFocus();
        if (this.status.i === this.data.length) {
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
                this.clear(this.status.flag);
                this.clear(this.status.flag + 1);
                this.clear(this.status.i);
                this.status.undo = ctx.getImageData(0, 0, frame.width, frame.height);
                this.swap(this.status.flag, this.status.flag + 1, this.status.i);
                this.status.move = [];
                this.status.current = 0;
                if (this.status.flag + 1 === this.status.i) {
                    this.status.move.push([this.status.flag, this.status.flag + 1]);
                    this.status.move.push([this.status.flag + 1, this.status.flag]);
                } else {
                    this.status.move.push([this.status.flag, this.status.flag + 1]);
                    this.status.move.push([this.status.flag + 1, this.status.i]);
                    this.status.move.push([this.status.i, this.status.flag]);
                }
                this.status.flag++;
                this.status.i++;
                return;
            }
            this.status.i++;
        }
        return;
    }

    if (size > 1) {
        this.status = {
            i: last.begin + 1,
            flag: last.begin,
            undo: undefined,
            move: undefined,
            current: undefined,
            time: 1000
        }
    } else {
        let tmp;
        do {
            tmp = this.stack.pop();
        } while (tmp !== undefined && !tmp.left);
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

Data.prototype.toCord = function (i) {
    let n = Math.floor(i / this.line);
    let m = i - n * this.line;
    return {
        n: n,
        m: m
    }
};

Data.prototype.clear = function (i) {
    let cord = this.toCord(i);
    this.data[i].clear(cord.m, cord.n);
};

Data.prototype.refresh = function (color, args) {
    this.line = Math.floor((frame.width - this.m2d) / this.dl);
    this.row = Math.ceil(this.data.length / this.line);
    frame.height = this.m2d + this.row * this.dl;
    setColor(color);
    let flag = 0;
    let i = 0;
    for (let n = 0; n < this.row; n++) {
        for (let m = 0; m < this.line; m++) {
            if (i === this.data.length) {
                return;
            }
            if (args.length > flag) {
                while (args.length > flag && args[flag].start <= i) {
                    if (args[flag].start === i) {
                        setColor(args[flag].color);
                    }
                    flag++;
                }
            }
            this.data[i].draw(m, n);
            i++;
        }
    }
};

Data.prototype.drawOther = function () {
    let last = this.stack[this.stack.length - 1];
    let lastLast = this.stack[this.stack.length - 2];
    if (this.stack.length > 1) {
        let args = [];
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
        this.refresh("green", args);
        this.strokeElement(lastLast.begin, lastLast.end, "gray");
    } else {
        this.refresh("white", []);
    }
    this.strokeElement(last.begin, last.end, "black");
};

Data.prototype.drawFocus = function () {
    let focus = this.stack[this.stack.length - 1];
    let flag = this.data[this.status.flag];
    let n = Math.floor(focus.begin / this.line);
    let m = focus.begin - n * this.line;
    for (let i = focus.begin; i < focus.end; i++) {
        if (this.data[i] > flag) {
            setColor("red");
        } else if (this.data[i] < flag) {
            setColor("green");
        } else {
            setColor("black");
        }
        this.data[i].fill(m, n);
        m++;
        if (m === this.line) {
            m = 0;
            n++;
        }
    }
};

Data.prototype.strokeElement = function (begin, end, color) {
    let bn = Math.floor(begin / this.line);
    let bm = begin - bn * this.line;
    let en = Math.floor(end / this.line);
    let em = end - en * this.line;
    if (em === 0 && en > 0) {
        en--;
        em = this.line;
    }
    if (en === bn + 1 && em < bm) {
        let cut = en * this.line;
        this.strokeElement(begin, cut, color);
        this.strokeElement(cut, end, color);
    } else if (en === bn) {
        let cord = Element.prototype.getXY(bm, bn);
        ctx.strokeStyle = color;
        ctx.strokeRect(cord.x - 2, cord.y - 2, (em - bm) * this.dl - distance + 4, length + 4);
    } else {
        let bxy = Element.prototype.getXY(bm, bn);
        bxy.x -= 2;
        bxy.y -= 2;
        let exy = Element.prototype.getXY(em, en);
        exy.x -= distance - 2;
        exy.y += 2 + length;
        let bx = this.md - 2;
        let by = bxy.y + this.dl;
        let rx = this.line * this.dl + margin + 2;
        let ry = exy.y - this.dl;
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
};

function path(begin, end, current, time) {
    let x = begin.x + Math.round((end.x - begin.x) * current / time);
    let y = begin.y + Math.round((end.y - begin.y) * current / time);
    return {x: x, y: y};
}

function setColor(color) {
    ctx.font = "bold 12pt sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = color;
    ctx.strokeStyle = color;
}

function ArgColor(start, color) {
    return {
        start: start,
        color: color
    };
}

function frames() {
    if (data.status !== undefined && data.status.move !== undefined && data.status.current <= data.status.time) {
        data.status.current += 40;
        ctx.putImageData(data.status.undo, 0, 0);
        for (let each of data.status.move) {
            let start = data.toCord(each[0]);
            let end = data.toCord(each[1]);
            start = Element.prototype.getXY(start.m, start.n);
            end = Element.prototype.getXY(end.m, end.n);
            let cord = path(start, end, data.status.current, data.status.time);
            if (data.data[each[1]] > data.data[data.status.flag]) {
                setColor("red");
            } else if (data.data[each[1]] < data.data[data.status.flag]) {
                setColor("green");
            } else {
                setColor("black");
            }
            data.data[each[1]].fillXY(cord.x, cord.y);
        }
    }
}

function resizeCanvas() {
    frame.width = window.innerWidth - 16;
    if (data.stack.length === 0) {
        data.refresh("green", []);
    } else {
        data.refresh("black", []);
    }
}

function getValue(event) {
    event = EventUtil.getEvent(event);
    EventUtil.preventDefault(event);
    size = form.elements["size"].value;
    data.stopSort();
    data = new Data(size);
    resizeCanvas();
}

function sortData() {
    data.id = setInterval("data.quickSort()", 1000);
    data.moveId = setInterval("frames()", 40);
    sort.disabled = true;
    window.onresize = null;
}

window.onresize = resizeCanvas;
data = new Data(size);
resizeCanvas();
EventUtil.addHandler(form, "submit", getValue);
