import axios from 'axios';
import {
	GET_BOOK,
	ERRORS
} from './types';

const API_URL = 'http://localhost:8080/api';

export function getBook(bookID) {
	const config = {
		path: `books/${bookID}`,
		type: GET_BOOK
	};

	return _get(config.path, {}, config.type);
}

function _get(path, config, type) {
	return (dispatch) => {
		axios.get(`${API_URL}/${path}/`, config)
			.then((response) => {
				dispatch({
					payload: response.data,
					type: type
				});
			})
			.catch((error) => {
				dispatch({
					payload: error,
					type: ERRORS
				});
			});
	};
}
