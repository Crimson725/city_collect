const getFirstEl = (className) => document.getElementsByClassName(className)[0];
const setTranslate = ($el, value) => $el.style.transform = `translateY(${value})`;

const elColEven = getFirstEl('js-ss-col-even');
const elColOdd = getFirstEl('js-ss-col-odd');
const btnPrev = getFirstEl('js-ss-prev');
const btnNext = getFirstEl('js-ss-next');
const stHalf = elColEven.childElementCount;
const ndHalf = elColOdd.childElementCount;
let page = 0;

function setOddToFirst() {
	const value = `-${100 / ndHalf * (ndHalf - 1)}%`;
	elColOdd.style.transition = 'none';
	setTranslate(elColOdd, value);
	setTimeout(() => elColOdd.style.transition = '');
}

function updateSliders() {
	setTranslate(elColEven, `-${(100 / stHalf) * page}%`);
	setTranslate(elColOdd, page === ndHalf
		? `${100 / ndHalf}%` // if goes beyond last when odd child
		: `-${(100 / ndHalf) * (ndHalf - 1 - page)}%`);
}

setOddToFirst();

btnPrev.addEventListener('click', () => {
	if (page === 0) { return false; }
	page--;
	return updateSliders();
});

btnNext.addEventListener('click', () => {
	if (page === stHalf - 1) { return false; }
	page++;
	return updateSliders();
});
