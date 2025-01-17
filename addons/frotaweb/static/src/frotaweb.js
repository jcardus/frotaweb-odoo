/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class Frotaweb extends Component {
    static template = "frotaweb.dashboard";
}

registry.category("actions").add("frotaweb.dashboard", Frotaweb);
