import React from 'react';
import {
	Form,
	Button
} from 'semantic-ui-react';

export default (props) => {
	return (
		<Form onSubmit={props.handleSubmit}>
			<Form.Field required>
				<label>Username</label>
				<input
					placeholder='Username'
					required
					value={props.values.username}
					onChange={props.handleChange}
					name='username'
					type='text'
				/>
			</Form.Field>
			<Form.Field required>
				<label>Password</label>
				<input
					placeholder='Password'
					required
					onChange={props.handleChange}
					value={props.values.password}
					name='password'
					type="password"
				/>
			</Form.Field>
			<Button type='submit' primary>Submit</Button>
		</Form>
	);
};
