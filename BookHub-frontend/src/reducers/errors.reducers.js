import {
	ERRORS,
	CLEAR_ERRORS
} from '../actions/types';

const INITIAL_STATE = {
	errorContent: {}
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case ERRORS:
			return {...state, errorContent: action.payload};
		case CLEAR_ERRORS:
			return {...state, errorContent: {}};
	}

	return state;
};
