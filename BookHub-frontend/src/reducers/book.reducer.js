import {
	GET_BOOK
} from '../actions/types';

const INITIAL_STATE = {
	bookData: {}
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case GET_BOOK:
			return {...state, bookData: action.payload};
	}

	return state;
};
