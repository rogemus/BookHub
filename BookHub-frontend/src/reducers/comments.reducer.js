import {
	GET_COMMENTS
} from '../actions/types';

const INITIAL_STATE = {
	list: []
};

export default (state = INITIAL_STATE, action) => {
	switch (action.type) {
		case GET_COMMENTS:
			return {...state, list: action.payload.results};
	}

	return state;
};
