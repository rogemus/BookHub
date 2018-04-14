import {
	ERRORS,
	CLEAR_ERRORS
} from '../actions/types';

export default (state = {}, action) => {
	switch (action.type) {
		case ERRORS:
			return {...state, errorContent: action.payload};
		case CLEAR_ERRORS:
			return {...state, errorContent: {}};
	}

	return state;
};
