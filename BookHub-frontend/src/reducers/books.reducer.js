import {
	GET_BOOKS
} from '../actions/types';

const INITIAL_STATE = {
	booksList: []
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case GET_BOOKS:
			return {...state, booksList: action.payload.results};
	}

	return state;
};
