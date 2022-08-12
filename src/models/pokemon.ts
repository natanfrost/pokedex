export interface Pokemon {
	id: number;
	name: string;
	height: number;
	weight: number;
	abilities: Abilities[];
	sprites: Sprites;
}

interface Abilities {
	id: number;
	name: string;
}

interface Sprites {
	versions: Versions;
}

interface Versions {
	genarationV: GenerationV;
}

interface GenerationV {
	blackWhite: BlackWhite;
}

interface BlackWhite {
	animated: Animated;
}

interface Animated {
	backDefault: string;
	frontDefault: string;
	backShiny: string;
	frontShine: string;
}
