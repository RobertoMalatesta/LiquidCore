/*
 * Copyright (c) 2016 - 2018 Eric Lange
 *
 * Distributed under the MIT License.  See LICENSE.md at
 * https://github.com/LiquidPlayer/LiquidCore for terms and conditions.
 */
package org.liquidplayer.service;

import android.view.View;

import org.liquidplayer.javascript.JSContext;
import org.liquidplayer.javascript.JSObject;
import org.liquidplayer.javascript.JSValue;

/**
 * A Surface is a UI interaction layer with a MicroService.
 */
public interface Surface {
    /**
     * A runnable to be called in the event of an error.  Do not call both the success and
     * failure runnables, or the result will be undefined behavior.  One or the other must
     * be called.
     */
    interface ReportErrorRunnable {
        /**
         * Method to be called to report an error
         * @param errorMessage The error message to report
         */
        void run(String errorMessage);
    }

    /**
     * Binds a surface to a MicroService. This gives the surface an opportunity to bind any native
     * functions required by the module.
     * @param service The microservice on which to bind
     * @param context The Javascript context on which to bind
     * @param export  An object which will be passed back to the caller where the surface may
     *                export its JS bindings
     * @param config  An optional configuration parameter passed from JavaScript
     * @param onBound A runnable which must be called once binding is complete
     * @param onError A runnable which should be called if binding fails
     */
    void bind(MicroService service, JSContext context, JSObject export, JSValue config,
              Runnable onBound, ReportErrorRunnable onError);

    /**
     * Attaches a MicroService to the UI.
     * @param service  The MicroService to attach
     * @param onAttached A runnable to be called after the UI is active
     * @param onError A runnable which should be called if attaching fails
     */
    View attach(MicroService service, Runnable onAttached, ReportErrorRunnable onError);

    /**
     * Detaches any currently attached MicroService.  The Surface may then be ready to be discarded
     * or reattached.
     */
    void detach();

    /**
     * Detaches and clears the Surface.  This is the preferred method when the Surface is to be
     * reused.  detach() may leave behind some UI state, as it expects that the MicroService may
     * later be re-attached.  reset() clears any UI state back to a fresh state.
     */
    void reset();
}
