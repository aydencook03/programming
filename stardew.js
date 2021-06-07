
function Crop(name, cost, sell, growth, cycle, artisan) {
	this.name = name; // name of crop
	this.cost = cost; // buy price of seed
	this.sell = sell; // sell price of crop
	this.growth = growth; // initial time to grow
	this.cycle = cycle; // time to regrow, false if it doesn't regrow
	this.artisan = artisan // artisan good information
	// example ==> this.artisan = {name: "Beer", sell: 200"}
}

Crop.prototype.profit = null;
Crop.prototype.wastedDays = null;

Crop.prototype.getProfit = function(days) {
	if(days >= this.growth) {
		const sinceGrown = days - this.growth;
		const cyclesDone = Math.floor(sinceGrown / (this.cycle || this.growth)) + 1;
		this.wastedDays = sinceGrown % (this.cycle || this.growth);

		if(this.artisan) {
			this.sell = this.artisan.sell;
		}

		this.profit = (cyclesDone * this.sell) - this.cost;

		if(!this.cycle) {
			this.profit -= (this.cost * (cyclesDone - 1));

			if(this.wastedDays) {
				//this.profit -= this.cost;
			}
		}

		if(this.artisan) {
			return `${this.profit} as ${this.artisan.name}, with ${this.wastedDays} wasted days`
		} else {
			return `${this.profit}, with ${this.wastedDays} wasted days`
		}
	}
	else {
		return `Planted ${this.growth - days} days too late: lost ${this.cost}`
	}
}

// All Prices Use Tiller Profession

const bluejazz = new Crop("Blue Jazz", 30, 55, 7, false);
const cauliflower = new Crop("Cauliflower", 80, 192, 12, false);
const garlic = new Crop("Garlic", 40, 66, 4, false);
const kale = new Crop("Kale", 70, 121, 6, false);
const parsnip = new Crop("Parsnip", 20, 38, 4, false);
const potato = new Crop("Potato", 50, 80, 6, false);
const rhubarb = new Crop("Rhubarb", 100, 242, 13, false);
const tulip = new Crop("Tulip", 20, 33, 6, false);
const coffee = new Crop("Coffee", 0, 15 * 4, 10, 2, {name: "Coffee Drink", sell: 150 * 1.4 * 4 / 5}); // produces 4 beans
const greenbean = new Crop("Green Beans", 60, 44, 10, 3);
const strawberry = new Crop("Strawberry", 100, 132, 8, 4);
const ancientfruit = new Crop("Ancient Fruit", 1000, 605, 28, 7);

const spring = [
	bluejazz, cauliflower, garlic, kale, parsnip, potato, rhubarb, tulip, coffee, greenbean, strawberry, ancientfruit
];

const wheat = new Crop("Wheat", 10, 27, 4, false, {name: "Beer", sell: 200 *1.4});
const sunflower = new Crop("Sunflower", 200, 88, 8, false);
const summerspangle = new Crop("Summer Spangle", 50, 123, 8, false);
const starfruit = new Crop("Starfruit", 400, 825, 13, false);
const redcabbage = new Crop("Red Cabbage", 100, 286, 9, false);
const radish = new Crop("Radish", 40, 99, 6, false);
const poppy = new Crop("Poppy", 100, 154, 7, false);
const melon = new Crop("Melon", 80, 275, 12, false);
const tomato = new Crop("Tomato", 50, 66, 11, 4);
const pepper = new Crop("Pepper", 40, 44, 5, 3);
// coffee
// ancientfruit
const hops = new Crop("Hops", 60, 27, 11, 1, {name: "Pale Ale", sell: 300*1.4});
const corn = new Crop("Corn", 150, 55, 14, 4, {name: "Oil", sell: 100*1.4});
const blueberry = new Crop("Blueberry", 80, 55 * 3, 13, 4); // produces 3 berries

const summer = [
	wheat, sunflower, summerspangle, starfruit, redcabbage, radish, poppy, melon, tomato, pepper, coffee, ancientfruit, hops, corn, blueberry
];

const pumpkin = new Crop("Pumpkin", 100, 352, 13, false);
const artichoke = new Crop("Artichoke", 30, 176, 8, false);
const beet = new Crop("Beet", 20, 110, 6, false);
const bokchoy = new Crop("Bok Choy", 50, 88, 4, false);
// wheat
const amaranth = new Crop("Amaranth", 70, 165, 4, false);
const sweetgemberry = new Crop("Sweet Gem Berry", 1000, 3000, 24, false);
const yam = new Crop("Yam", 60, 176, 10, false);
// sunflower
const fairyrose = new Crop("Fairy Rose", 200, 319, 12, false);
// corn
// ancient fruit
const eggplant = new Crop("Eggplant", 20, 66, 5, 5);
const cranberries = new Crop("Cranberries", 240, 82 * 2, 7, 5); // produces 2 berries
const grapes = new Crop("Grapes", 60, 88, 10, 3);

const fall = [
	pumpkin, artichoke, beet, bokchoy, wheat, amaranth, sweetgemberry, yam, sunflower, fairyrose, corn, ancientfruit, eggplant, cranberries, grapes
];


let all = new Set([...spring, ...summer, ...fall]);


let season = prompt("What Season? ==> ");
season == 'spring' ? season = spring : season == 'summer' ? season = summer : season == 'fall' ? season = fall : season = all;
const day = prompt("What Day of the Season? ==> ");


for(const crop of season) {
	if(crop.name !== "Coffee" && crop.name !== "Wheat" && crop.name !== "Corn") {
		const daysLeft = 28 - day;
		console.log(`${crop.name}: ${crop.getProfit(daysLeft)}`);
	}
	else if(crop.name == "Coffee") {
		if(season == spring) {
			const daysLeft = 56 - day;
			console.log(`${crop.name}: ${crop.getProfit(daysLeft)} over next season`);
		} else {
			const daysLeft = 28 - day;
			console.log(`${crop.name}: ${crop.getProfit(daysLeft)}`);
		}
	}
	else if(crop.name == "Wheat") {
		if(season == summer) {
			const daysLeft = 56 - day;
			console.log(`${crop.name}: ${crop.getProfit(daysLeft)} over next season`);
		} else {
			const daysLeft = 28 - day;
			console.log(`${crop.name}: ${crop.getProfit(daysLeft)}`);
		}
	}
	else if(crop.name == "Corn") {
		if(season == summer) {
			const daysLeft = 56 - day;
			console.log(`${crop.name}: ${crop.getProfit(daysLeft)} over next season`);
		} else {
			const daysLeft = 28 - day;
			console.log(`${crop.name}: ${crop.getProfit(daysLeft)}`);
		}
	}
}


/*
- Qi battery pack
- honey + fairy roses in greenhouse
*/