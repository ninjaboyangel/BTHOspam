import React, { Component } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import Header from './components/Header/Header'
import Home from './components/Home/Home'
import Dashboard from './components/Dashboard/Dashboard';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
        <Header />
          <Switch>
            <Route exact path='/' component={Home} />
            <Route path='/dashboard' component={Dashboard} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
