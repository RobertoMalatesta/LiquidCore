/*
 * Copyright (c) 2014 - 2018 Eric Lange
 *
 * Distributed under the MIT License.  See LICENSE.md at
 * https://github.com/LiquidPlayer/LiquidCore for terms and conditions.
 */
package org.liquidplayer.javascript;

import org.junit.Test;

import java.util.Arrays;

import static org.junit.Assert.*;

public class JSIteratorTest {

    @Test
    public void testJSIterator() throws Exception {
        JSContext context = new JSContext();
        testJSIterator(context);
    }

    public void testJSIterator(JSContext context) throws Exception {
        JSArray<Integer> array = new JSArray<>(context, Arrays.asList(0,1,2,3,4), Integer.class);
        JSArray.KeysIterator iterator = array.keys();

        int i=0;
        for(; iterator.hasNext(); i++) {
            assertEquals(iterator.next(),array.get(i));
            boolean exception = false;
            try {
                iterator.remove();
            } catch (UnsupportedOperationException e) {
                exception = true;
            } finally {
                assertTrue(exception);
            }
        }
        assertEquals(i,array.size());
    }
}