import React, {Component} from 'react';
import {connect} from 'react-redux';
import {postUserCredential} from '../../actions/authentication.actions';
import LoginForm from '../../components/loginForm/loginForm.component';

class LoginPage extends Component {
	constructor(props) {
		super(props);

		this.state = {
			email: '',
			password: ''
		};
	}

	renderLoginForm() {
		return (
			<LoginForm
				handleSubmit={this.onSubmit.bind(this)}
				handleChange={this.onChange.bind(this)}
				values={{email: this.state.email, password: this.state.password}}
			/>
		);
	}

	onSubmit($event) {
		const userData = {
			email: this.state.email,
			password: this.state.password
		};

		$event.preventDefault();
		this.props.postUserCredential(userData);
	}

	onChange($event) {
		this.setState({[$event.target.name]: $event.target.value});
	}

	render() {
		return (
			<div>
				{this.renderLoginForm()}
			</div>
		);
	}
}

function mapStateToProps(state) {
	return {
		user: state.book.bookData
	};
}

export default connect(mapStateToProps, {postUserCredential})(LoginPage);

