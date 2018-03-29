import {ERRORS} from './types';

export function clearErrors() {
	return (dispatch) => {
		return dispatch({
			type: ERRORS
		});
	};
}
