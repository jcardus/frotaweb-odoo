/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { user } from "@web/core/user";



class Frotaweb extends Component {
    static template = "frotaweb.dashboard";

    setup() {
        super.setup();
        this.state = useState({iframeSrc: ""});
        this.orm = useService("orm");

        onWillStart(this.updateFrame);
    }

    async updateFrame() {
        const userData = await this.orm.call("res.users", "search_read", [[['id', '=', user.userId]]])
        this.state.iframeSrc = `https://dash.frotaweb.com/traccar?token=${userData[0].traccar_token}`;
    }
}

registry.category("actions").add("frotaweb.dashboard", Frotaweb);
