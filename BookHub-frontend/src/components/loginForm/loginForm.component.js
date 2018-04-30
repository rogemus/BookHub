import React from 'react';
import PropTypes from 'prop-types';

export default function LoginForm(props) {
	return (
		<form onSubmit={props.handleSubmit} className="form">
			<div className='form-field'>
				<label htmlFor='username'>Username</label>
				<input
					placeholder='Username'
					required
					value={props.values.username}
					onChange={props.handleChange}
					name='username'
					type='text'
					id='username'
				/>
			</div>
			<div className='form-field'>
				<label htmlFor='password'>Password</label>
				<input
					placeholder='Password'
					required
					onChange={props.handleChange}
					value={props.values.password}
					name='password'
					type="password"
					id='password'
				/>
			</div>
			<button className="btn" type='submit'>Submit</button>
		</form>
	);
}

LoginForm.propTypes = {
	handleSubmit: PropTypes.func.isRequired,
	handleChange: PropTypes.func.isRequired,
	values: PropTypes.object.isRequired
};
