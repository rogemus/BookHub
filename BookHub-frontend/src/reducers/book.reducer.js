import {
	GET_BOOK
} from '../actions/types';

export default (state = {}, action) => {
	switch (action.type) {
		case GET_BOOK:
			return {...state, book: action.payload};
	}

	return state;
};
